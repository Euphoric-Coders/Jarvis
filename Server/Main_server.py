import glob, os

servers = {"PRERAK":"DESKTOP-B3GC6VI",
           "SAMAY":"DESKTOP-12OV957",
           "SAM":"VKGLaptop",
           "DJ":"DESKTOP-7C1T3TI"}

cur_server = servers["SAMAY"]

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
    dists, nms, add_txt = Dist(classified)
    print(add_txt)
    val = list(object_dictionary.keys())
    l = []
    updated = []
    for i in range(len(val)):
        each = val[i]
        if txt == "assist":
            ds = min(dists)
            ind = dists.index(ds)
            ds = round(ds)
            obj = nms[ind]
            ad_txt = add_txt[ind]
            op_txt = obj + " is " + str(ds) + " steps ahead" + ad_txt

        elif txt == "vis":
            for i in range(len(nms)):
                ds = round(dists[i])
                obj = nms[i]
                ad_txt = add_txt[i]
                op_txt = obj + " is " + str(ds) + " steps ahead" + ad_txt
                l.append(op_txt)
            
        elif each in txt:
            obj = each
            if obj in nms:
                ind = nms.index(obj)
                ds = round(dists[ind])
                ad_txt = add_txt[ind]
                print(ad_txt, add_txt,ind)
                op_txt = obj + " is " + str(ds) + " steps ahead" + ad_txt
            else:
                print(obj)
                print(nms)
                op_txt = "object not found er1"
            if txt != "vis":
                break
        elif i == len(val)-1:
            op_txt = "object not found"

    if txt == "vis":
        for each in l:
            if each not in updated:
                updated.append(each)
        send_txt(str(updated))
    else:
        send_txt(op_txt)

