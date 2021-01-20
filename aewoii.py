import os
from time import sleep

# a(kuning) b (red) c (greenlight) d (bluelight) e (white)

a ='\033[1;33m'
b ='\033[31;1m'
c ='\033[32;1m'
d ='\033[36;1m'
e ='\033[37;1m'
os.system('clear')
print(a+'\t ❑ Keyboard' +e+'Termux')
print(c+'\t ❑ Instagram ➣' +a+'https://instagram.com/ae_fight')
print(c+'\t ❑ Telegram  ➢' +a+'https://t.me/aewoii')
print(c+'\t ❑ Github    ➢' +a+'https://github.com/aeroyals/keyboard')
print('\t ────────────────────────────────────────────────────────────')
print(a+'+'*40)
print('\nProses..')
sleep(5)
print(b+'\n[!] Mngambil Data Termux!')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(3)
print(b+'\n[!] Memasang Keyboard...')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Sedang Proses... !')
sleep(1)
print(b+'\n[!] Tunggu Sebentar...')
sleep(5)
os.system('termux-reload-settings')
print(a+'[!] Proses Selesai !! ^^')
