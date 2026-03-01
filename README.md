macOS에서 한글파일을 생성할때 파일명의 한글이 분리되는 현상이 있다. 
NFD (Normalization Form Canonical Decomposition): 한글을 자음과 모음으로 분리하여 저장하는 방식 (주로 macOS).
NFC (Normalization Form Canonical Composition): 한글을 하나의 완성된 글자로 저장하는 방식 (주로 Windows).
해당 방식의 충돌로 인해 분리된 자모를 다시 합친다
