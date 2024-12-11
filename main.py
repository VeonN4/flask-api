from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    return jsonify({'data': "Watashi no na wa Kira Yoshikage. Renrei sanjyuu sansai. Jitaku wa Morioh-cho hokuto no bu no bessojidai ni ari, kekkon wa shiite-inai, Shigoto wa Kame-yu chen-ten no kai sha-in de, maiinichi osokuto mo yoru hachii-ji made ni wa kitakusuru. Tabaco-o wa sumanai, sake wa tashinamu-tedo, yoru juu-ichi ji ni wa toko nitsukii, kanarazu hajii-jikan wa suii-min o toru yo-o ni shiiteiru. Neru mae ni at-ta-kae miruuku o nomi ni-juu pun hodo no suutorechi de karada o homu-shite kara toko nitsuku-to hodon do asa made jukusui-sa. Akanbo no yo ni hiro ya suutoresu o noku sazu nii asa me o samaserunda. Kenko-o shintan de mo ijyo nashito iwaretaiyo. Watashi wa tsune nii kokoro o heion o ne-gate ik-terun ningen toyukoto o setsumei-shite-iru no dai-yo. Kachi make ni koda wa-tari, atama o kakaeruyoo na torabuuruu to ka, yoru mo nemurenai to ita teki o tsukuranai. Toyuu no ga watashii no shakai ni taisuru shise de ari, sorega jibun no kofuku da to toyuukoto o shiteiru. Mo-tomo tatakatte da toshitemo, watashi wa dare ni mo makenn ga ne..."})

@app.route('/password/<int:length>', methods = ['GET'])
def create_password(length):
    characterList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+=-[]{}\|/?.>,<`~"
    password = []

    for i in range(length):
        random_character = random.choice(characterList)
        password.append(random_character)

    return jsonify({'data': "".join(password)})

@app.route('/palindrome/<int:num>')
def palindrome(num: int):
    if num < 0:
        return False
    
    global reversedNum

    reversedNum = 0
    temp = num

    while temp != 0:
        digit = temp % 10
        reversedNum = reversedNum * 10 + digit
        temp //= 10

    return jsonify({'data': (reversedNum == num)})

# driver function 
if __name__ == '__main__':
    app.run() 

