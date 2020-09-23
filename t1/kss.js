var slides=document.querySelector('.slides'),
slide=document.querySelectorAll('.slides li'),
currentIdx=0,
slideCount=slide.length,
prevBtn=document.querySelector('.prev'),
nextBtn=document.querySelector('.next'),
slideWidth=400;

slides.style.width=slideWidth*slideCount+'px';
function moveSlide(num){
    slides.style.left=-num*400+'px';
    currentIdx=num;
}
nextBtn.addEventListener('click',function(){
    if(currentIdx<slideCount-1){
        moveSlide(currentIdx+1);
        console.log(currentIdx);
    }
    else{
        moveSlide(0);
    }
});
prevBtn.addEventListener('click',function(){
    if(currentIdx>0){
        moveSlide(currentIdx-1);
        console.log(currentIdx);
    }
    else{
        moveSlide(slideCount-1);
    }
});