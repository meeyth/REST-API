from flask import Flask, jsonify, request
import database_handler.db_handler as db_handler

app = Flask(__name__)


@app.get('/user-data/<int:_id>')
def home(_id):
    res = db_handler.get_data(_id)
    if res:
        return res

    res = jsonify("NOT FOUND!")
    res.status_code = 404
    return res


@app.post('/user-data')
def homePost():
    body = request.get_json()
    body |= {'_id': db_handler.collection_len() + 1}
    try:
        db_handler.post_data(body)
    except Exception as e:
        res = jsonify(
            {'errmsg': 'Document failed validation',
             'required': ['name', 'username', 'age'],
             }
        )
        res.status_code = 500
        return res
    return jsonify(body)


@app.put('/user-data/<int:_id>')
def homePut(_id):
    body = request.get_json()

    try:
        db_handler.put_data(body, _id)
    except Exception as e:
        res = jsonify(
            {'errmsg': 'Document failed validation',
             'required': ['name', 'username', 'age'],
             }
        )
        res.status_code = 500
        return res

    return body


@app.delete('/user-data/<int:_id>')
def homeDelete(_id):
    res = db_handler.delete_data(_id)
    if res:
        return res

    res = jsonify("NOT FOUND!")
    res.status_code = 404
    return res


@app.patch('/user-data/<int:_id>')
def homePatch(_id):
    body = request.get_json()
    res = db_handler.patch_data(body, _id)
    if res:
        return res

    res = jsonify("NOT FOUND!")
    res.status_code = 404
    return res


if __name__ == "__main__":
    app.run(debug=True)
