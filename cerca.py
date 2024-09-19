import os

def CercaStringaInNomeFile(sFile, sStringa):
    #mettiamo minuscolo
    sFileLower= sFile.lower()
    sStringaLower = sStringa.lower()

    if (sFileLower.find(sStringaLower)>= 0):
        return True
    else:
        return False

def CercaStringaInContenutoFile(sPathFile, sStringa):
    bRet = False
    sOutFileName, sOutFileExt = os.path.splitext(sPathFile)
    if sOutFileExt.lower() == ".txt":
        bRet = CercaStringaInTextFile(sPathFile, sStringa)
    
    if sOutFileExt.lower() == ".pdf":
        bRet = CercaStringaInPDFfile(sPathFile, sStringa)

    return bRet

    #usiamo sFileLower.find() che torna -1 se la parola non c'è e la pos altrimenti
    #torniamo true oppure false
    

sRoot = input("Inserisci directory in cui cercare: ")
sParola = input("Inserisci parola da cercare: ")
sOutDir = input("Inserici directory di output: ")

iNumFileTrovati = 0
for root, dirs, files in os.walk(sRoot):
    print(f"Sto guardando {root} che contiene {len(dirs)} subdir e {len(files)} files")
    for file in files:
        print(f"Devo vedere se {file} contiene {sParola}")

        bRet = CercaStringaInNomeFile(file, sParola)
        if bRet == True:
            iNumFileTrovati += 1
        else:
            sFilePathCompleto = os.path.join(root,file)
            bRet = CercaStringaInContenutoFile(sFilePathCompleto,sParola)
            if (bRet == True):
                iNumFileTrovati +=1

    print(f"Ho trovato {iNumFileTrovati} files")