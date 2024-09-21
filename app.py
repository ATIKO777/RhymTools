from flask import Flask, jsonify, request
from utils.generator import ChordsGen
from flasgger import Swagger
from utils.harmonizer import Harmonizer
from utils.melodizer import Melodizer
from utils.chord import Chord

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

# Гармонизация мелодии
@app.route('/harmonize', methods=['GET'])
def harmonize():
    """
    Harmonize melody
    ---
    parameters:
      - name: motif
        in: query
        type: string
        required: true
        description: list of some notes
        example: C,D,E
    responses:
      200:
        description: A list of chords
        schema:
          type: array
    """
    input_motif = request.args.get('motif')
    motif = input_motif.split(',')

    if not input_motif:
        return jsonify({"error": "No input data provided"}), 400

    harmonizer = Harmonizer()
    harmonizer.harmonize(motif)

    chords = []
    for chord in harmonizer.chords:
        chords.append(chord.name)

    if chords:
        return jsonify(chords)
    else:
        return jsonify({'message': 'Harmonize Error'}), 500
    
# Мелодизация аккордов (возвращает звукоряд целиком)
@app.route('/melodize', methods=['GET'])
def melodize():
    """
    Melodize chord
    ---
    parameters:
      - name: base_note
        in: query
        type: string
        required: true
        description: base note of chord (tonic)
        example: C#
      - name: quality
        in: query
        type: string
        required: true
        description: quality of chord
        example: major
    responses:
      200:
        description: A list of notes
        schema:
          type: array
    """
    base_note = request.args.get('base_note')
    quality = request.args.get('quality')
    chord = Chord(base_note, quality)

    if not chord:
        return jsonify({"error": "No input data provided"}), 400

    melodizer = Melodizer()
    melodizer.melodize(chord)

    notes = melodizer.notes

    if notes:
        return jsonify(notes)
    else:
        return jsonify({'message': 'Melodize Error'}), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
