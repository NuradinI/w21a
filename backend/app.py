from flask import Flask, request, Response
import mariadb
import dbcreds
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/blogpostings', methods = ['GET', 'POST', 'PATCH', 'DELETE'])
def blogpostings():
    if request.method == 'GET':
        conn = None
        cursor = None
        posts = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, user=dbcreds.user)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM blog')
            posts = cursor.fetchall()
        except Exception as error:
            print('Something went wrong!')
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(posts != None):
                return Response(json.dumps(posts, default=str), mimetype='application/json', status = 200)
            else:
                return Response(json.dumps(posts, default=str), mimetype='text/html', status = 500)

    elif request.method == 'POST':
        conn = None
        cursor = None
        rows = None
        blog_description = request.json.get('description')
        blog_createdAt = request.json.get('created_at')
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, user=dbcreds.user)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO blog(description, created_at) VALUES (?, ?)', [blog_description, blog_createdAt])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error: 
            print('Oops!, something went wrong')
            print(error)
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response('Blog posted!', mimetype='application/json', status = 201)
            else:
                return Response('Post Failed...', mimetype='text/html', status=500)

    elif request.method == 'PATCH':
        conn = None
        cursor = None
        blog_description = request.json.get('description')
        blog_createdAt = request.json.get('created_at')
        blog_id = request.json.get('id')
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, user=dbcreds.user)
            cursor = conn.cursor()

            if blog_description != '' and blog_description != None:
                cursor.execute('UPDATE blog SET description=? WHERE id=?', [blog_description, blog_id ])
            conn.commit()
            rows = cursor.rowcount()
        except Exception as error:
            print('Oops! Something went wrong')
            print(error)

        finally: 
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if (rows == 1):
                return Response('Successful Update!', mimetype='application/json', status=204)
            else:
                return Response('Update Failed...', mimetype='text/html', status=500)

    elif request.method == 'DELETE':
        conn = None
        cursor = None
        blog_id = request.json.get('id')
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, user=dbcreds.user)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM blog WHERE id=?', [blog_id,])
            conn.commit()
            rows = cursor.rowcount

        except Exception as error:
            print('Something went wrong')
            print(error)
        finally:
            if cursor != None:
                    cursor.close()
            if conn != None:
                    conn.rollback()
                    conn.close()
            if (rows == 1):
                    return Response('Successful Delete!', mimetype='text/html', status=204)
            else:
                    return Response('Update failed...', mimetype='text/html', status=500)





    
