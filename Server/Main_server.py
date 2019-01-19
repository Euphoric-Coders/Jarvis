import glob, os

os.chdir("Subfiles\\")
files = glob.glob("*.py")
for eachfile in files:
    fl = open(eachfile)
    scrpt = fl.read()
    exec(scrpt)
    fl.close()

running = True
while running:
    txt = recv_txt()
    file = recv_img()
    classified = Detect(file)
    txt = classified[0]
    send_txt(txt)
    input()
