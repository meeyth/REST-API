from flask import Flask, jsonify, request
from controller import controller

app = Flask(__name__)


@app.get('/user-data/<int:_id>')
def home(_id):
    res = controller.get_data(_id)
    if res:
        return res

    res = jsonify("NOT FOUND!")
    res.status_code = 404
    return res


@app.post('/user-data')
def homePost():
    body = request.get_json()
    body |= {'_id': controller.collection_len() + 1}
    try:
        controller.post_data(body)
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
        controller.put_data(body, _id)
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
    res = controller.delete_data(_id)
    if res:
        return res

    res = jsonify("NOT FOUND!")
    res.status_code = 404
    return res


@app.patch('/user-data/<int:_id>')
def homePatch(_id):
    body = request.get_json()
    res = controller.patch_data(body, _id)
    if res:
        return res

    res = jsonify("NOT FOUND!")
    res.status_code = 404
    return res


if __name__ == "__main__":
    app.run(debug=True)
