#!python
#-*- coding: utf-8 -*-
print("content-type: text/html; charset-utf-8\n") #헤더를 전송해주는 코드 헤더에는 줄바꿈이 반드시 필요
import sys
import codecs

# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
form = cgi.FieldStorage()
pageId = form.getvalue('id') #왜 이거일까? 문법이 다 조금씩 다른듯? 형식오류 
print(pageId)
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
                        <a style="list-style-type: none;" href="h2-2.html"><span>SIH</span></a>
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
    <div class="box2">
        <div class="video">
            <video loop autoplay muted src="carvideo.mp4">
           </video>
        </div>
    </div>
   <div class="text1">
       <h1 style="font-size: 40px;">WelCome To DonTan Degaris</h1>
   </div>
   <div>
       <div #grid>
           <img class="photo1" src="IMG_6594.JPG">
           <img class="photo2" src="IMG_6725.JPG">
           <img class="photo3" src="IMG_8480.JPG">
       </div>
   </div>
   <div style="text-align: center;">
       <h1>2017.OSAKA</h1>
       <h2>KSS SIH KJC CJY CRAYON</h2>
   </div>
   <div class="slide_wrapper">
       <ul class="slides">
           <li><img class="imgsize" src="IMG_6425.JPG" alt=""></li>
           <li><img class="imgsize" src="IMG_6442.JPG" alt=""></li>
           <li><img class="imgsize" src="IMG_6466.JPG" alt=""></li>
           <li><img class="imgsize" src="IMG_8745.JPG" alt=""></li>
           <li><img class="imgsize" src="IMG_6427.JPG" alt=""></li>
           <li><img class="imgsize" src="IMG_8718.JPG" alt=""></li>
           <li><img class="imgsize" src="IMG_6449.JPG" alt=""></li>
           <li><img class="imgsize"src="IMG_8751.JPG" alt=""></li>
           <li><img class="imgsize" src="IMG_8753.JPG" alt=""></li>
           <li><img class="imgsize"src="IMG_8749.JPG" alt=""></li>
           <li><img class="imgsize"src="IMG_6725.JPG" alt=""></li>
      </ul>
    <p class="controls">
        <span class="prev">prev</span>
        <span class="next">next</span>
    </p>



   </div>
   
 <!-- 아 씨발 이거 순서있는 프로그램이라서 맨뒤에 놨뒀어야함;;;;;
그래서 처음 body 테그만 인식할 수 있엇다....왜냐면 헤드에 놨두니까 헤드는 바디 맨처음에 적용이 되버려서 그렇다.-->  
 <script type="text/javascript" src="kss.js"></script>

 
</body>
</html>''')
  