from flask import Flask, jsonify, request
from utils.generator import ChordsGen
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


# Генерация аккордов
@app.route('/generate', methods=['GET'])
def generate():
    """
    Generate chords
    ---
    parameters:
      - name: count
        in: query
        type: integer
        required: true
        description: count of chords
      - name: start_note
        in: query
        type: string
        required: true
        description: First Tonic
      - name: start_quality
        in: query
        type: string
        required: true
        description: Quality of first chord
    responses:
      200:
        description: A list of chords
        schema:
          type: array
    """
    count = int(request.args.get('count'))
    start_note = request.args.get('start_note')
    start_quality = request.args.get('start_quality')

    if not count or not start_note or not start_quality:
        return jsonify({"error": "No input data provided"}), 400

    generator = ChordsGen(start_note, start_quality)
    generator.generate(count)

    chords = []
    for chord in generator.chords:
        chords.append(chord.name)

    if chords:
        return jsonify(chords)
    else:
        return jsonify({'message': 'Generation Error'}), 500


if __name__ == '__main__':
    app.run(debug=False)
