from flask import Flask, render_template, request, jsonify
from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher
from cipher.vigenere import VigenereCipher 
import os

app = Flask(__name__)

# Router routes for home page
@app.route('/')
def home():
    return render_template('index.html')

# Router routes for caesar cipher
@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

# Router routes for Caesar encryption
@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    try:
        data = request.form
        text = data.get('inputText', '').strip()  # Cập nhật tên trường
        key = int(data.get('inputKey', 0)) % 26   # Cập nhật tên trường
        
        if not text:
            return jsonify({'error': 'Plain text is required'}), 400
        
        caesar = CaesarCipher()
        encrypted_text = caesar.encrypt_text(text, key)
        return jsonify({
            'text': text,
            'key': key,
            'encrypted_text': encrypted_text
        })
    except ValueError:
        return jsonify({'error': 'Invalid key, must be a number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Router routes for Caesar decryption
@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    try:
        data = request.form
        text = data.get('inputText', '').strip()  # Cập nhật tên trường
        key = int(data.get('inputKey', 0)) % 26   # Cập nhật tên trường
        
        if not text:
            return jsonify({'error': 'Cipher text is required'}), 400
        
        caesar = CaesarCipher()
        decrypted_text = caesar.decrypt_text(text, key)
        return jsonify({
            'text': text,
            'key': key,
            'decrypted_text': decrypted_text
        })
    except ValueError:
        return jsonify({'error': 'Invalid key, must be a number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Playfair Cipher Encryption
@app.route('/playfair_encrypt', methods=['POST'])
def playfair_encrypt():
    try:
        data = request.form
        text = data.get('inputText', '').strip()
        key = data.get('inputKey', '').strip()
        
        if not text or not key:
            return jsonify({'error': 'Text and key are required'}), 400
        
        playfair = PlayFairCipher()
        matrix = playfair.create_playfair_matrix(key)
        encrypted_text = playfair.playfair_encrypt(text, matrix)
        return jsonify({
            'text': text,
            'key': key,
            'encrypted_text': encrypted_text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Playfair Cipher Decryption
@app.route('/playfair_decrypt', methods=['POST'])
def playfair_decrypt():
    try:
        data = request.form
        text = data.get('inputText', '').strip()
        key = data.get('inputKey', '').strip()
        
        if not text or not key:
            return jsonify({'error': 'Text and key are required'}), 400
        
        playfair = PlayFairCipher()
        matrix = playfair.create_playfair_matrix(key)
        decrypted_text = playfair.playfair_decrypt(text, matrix)
        return jsonify({
            'text': text,
            'key': key,
            'decrypted_text': decrypted_text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rail Fence Cipher Encryption
@app.route('/railfence_encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        data = request.form
        text = data.get('inputText', '').strip()
        key = int(data.get('inputKey', 0))
        
        if not text or key < 2:
            return jsonify({'error': 'Text is required and key must be at least 2'}), 400
        
        railfence = RailFenceCipher()
        encrypted_text = railfence.rail_fence_encrypt(text, key)
        return jsonify({
            'text': text,
            'key': key,
            'encrypted_text': encrypted_text
        })
    except ValueError:
        return jsonify({'error': 'Invalid key, must be a number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rail Fence Cipher Decryption
@app.route('/railfence_decrypt', methods=['POST'])
def railfence_decrypt():
    try:
        data = request.form
        text = data.get('inputText', '').strip()
        key = int(data.get('inputKey', 0))
        
        if not text or key < 2:
            return jsonify({'error': 'Text is required and key must be at least 2'}), 400
        
        railfence = RailFenceCipher()
        decrypted_text = railfence.rail_fence_decrypt(text, key)
        return jsonify({
            'text': text,
            'key': key,
            'decrypted_text': decrypted_text
        })
    except ValueError:
        return jsonify({'error': 'Invalid key, must be a number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Transposition Cipher Encryption
@app.route('/transposition_encrypt', methods=['POST'])
def transposition_encrypt():
    try:
        data = request.form
        text = data.get('inputText', '').strip()
        key = int(data.get('inputKey', 0))
        
        if not text or key < 1:
            return jsonify({'error': 'Text is required and key must be at least 1'}), 400
        
        transposition = TranspositionCipher()
        encrypted_text = transposition.encrypt(text, key)
        return jsonify({
            'text': text,
            'key': key,
            'encrypted_text': encrypted_text
        })
    except ValueError:
        return jsonify({'error': 'Invalid key, must be a number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Transposition Cipher Decryption
@app.route('/transposition_decrypt', methods=['POST'])
def transposition_decrypt():
    try:
        data = request.form
        text = data.get('inputText', '').strip()
        key = int(data.get('inputKey', 0))
        
        if not text or key < 1:
            return jsonify({'error': 'Text is required and key must be at least 1'}), 400
        
        transposition = TranspositionCipher()
        decrypted_text = transposition.decrypt(text, key)
        return jsonify({
            'text': text,
            'key': key,
            'decrypted_text': decrypted_text
        })
    except ValueError:
        return jsonify({'error': 'Invalid key, must be a number'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Vigenere Cipher Encryption
@app.route('/vigenere_encrypt', methods=['POST'])
def vigenere_encrypt():
    try:
        data = request.form
        text = data.get('inputText', '').strip()
        key = data.get('inputKey', '').strip()
        
        if not text or not key:
            return jsonify({'error': 'Text and key are required'}), 400
        
        vigenere = VigenereCipher()
        encrypted_text = vigenere.vigenere_encrypt(text, key)
        return jsonify({
            'text': text,
            'key': key,
            'encrypted_text': encrypted_text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Vigenere Cipher Decryption
@app.route('/vigenere_decrypt', methods=['POST'])
def vigenere_decrypt():
    try:
        data = request.form
        text = data.get('inputText', '').strip()
        key = data.get('inputKey', '').strip()
        
        if not text or not key:
            return jsonify({'error': 'Text and key are required'}), 400
        
        vigenere = VigenereCipher()
        decrypted_text = vigenere.vigenere_decrypt(text, key)
        return jsonify({
            'text': text,
            'key': key,
            'decrypted_text': decrypted_text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)