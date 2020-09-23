#!python
a=3+4+5
b=a/3
print("content-type: text/html; charset-utf-8\n") #헤더를 전송해주는 코드 헤더에는 줄바꿈이 반드시 필요
print('''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KSS HOMEPAGE</title>
    <meta property="og:type" content="website"/>
    <meta property="og:title" content="KSS2 website"/>
    <meta property="og:description" content="Test2 website"/>
    <meta property="og:image" content="IMG_i896.PNG"/>
    <link rel='stylesheet' href="kstyle2.css">
   
    
    
 
</head>
<body>
 <nav id="box" class="firstbox">
        <ul style="list-style-type: none;" class="firstbaner">
            <li class="banercont">
                <h1>D.T.D</h1>
            </li>    
            <input type="checkbox" id="menuicon">
            <label for="menuicon">
                <span></span>
                <span></span>
                <span></span>
            </label>
            <div class="slidebar">
                <h3 class="sidemenu">MENU</h3>
                <ul style="list-style-type: none;">
                    <li class="sidecontent">
                        <span>KSS</span>
                    </li>
                    <li class="sidecontent">
                        <span>LGS</span>
                    </li>
                    <li class="sidecontent">
                        <span>KJC</span>
                    </li>
                    <li class="sidecontent">
                        <span>SIH</span>
                    </li>
                    <li class="sidecontent">
                        <span>PYH</span>
                    </li>
                    <li class="sidecontent">
                        <span>CJY</span>
                    </li>
                    <li class="sidecontent">
                        <span>AHM</span>
                    </li>
                    <li class="sidecontent">
                        <span>PJI</span>
                    </li>
                    <li class="sidecontent">
                        <span>LHS</span>
                    </li>
                    <div>
                        HOME
                    </div>
                </ul>

            </div>
        </ul>   
    </nav>


</body>        
</html>
      ''')

