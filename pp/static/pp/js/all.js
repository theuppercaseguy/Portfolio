
const close_click = document.querySelector(".close-lt");
const lt = document.querySelector(".LT");

function slideup(){
    const classNames = lt.className.split(' ');
    classNames.forEach(name =>{
        if(name == "close-down"){
            lt.classList.remove("close-down");
        }
    });
    lt.classList.add("close-up");
}

function slidedown(){    
    const classNames = lt.className.split(' ');
    classNames.forEach(name =>{
        if(name == "close-up"){
            lt.classList.remove("close-up");
        }
    });
    lt.classList.add("close-down");
}

function inc_scroll_size(button){
    // alert("asdf");
    const barslist = document.querySelectorAll('.scrol-btts');
    console.log(barslist);

    const classnames1 = barslist[0].className.split(' ');
    const classnames2 = barslist[1].className.split(' ');
    const classnames3 = barslist[2].className.split(' ');
    const classnames4 = barslist[3].className.split(' ');
    
    classnames1.forEach(name =>{
        if(name == "dec-size"){
            barslist[0].classList.remove("dec-size");
        }
    })
    classnames2.forEach(name =>{
        if(name == "dec-size"){
            barslist[1].classList.remove("dec-size");
        }
    })
    classnames3.forEach(name =>{
        if(name == "dec-size"){
            barslist[2].classList.remove("dec-size");
        }
    })
    classnames4.forEach(name =>{
        if(name == "dec-size"){
            barslist[3].classList.remove("dec-size");
        }
    })


    if(button=="bt1"){
        barslist[0].classList.add("inc-size");
        barslist[1].classList.add("dec-size");
        barslist[2].classList.add("dec-size");
        barslist[3].classList.add("dec-size");
          
        console.log(classnames1);
    }
    else if(button=="bt2"){    
        barslist[0].classList.add("dec-size");
        barslist[1].classList.add("inc-size");
        barslist[2].classList.add("dec-size");
        barslist[3].classList.add("dec-size");
        
        
        console.log(classnames2);
    }
    else if(button=="bt3"){
        barslist[0].classList.add("dec-size");
        barslist[1].classList.add("dec-size");
        barslist[2].classList.add("inc-size");
        barslist[3].classList.add("dec-size");

        console.log(classnames3);
    }
    else if(button=="bt4"){
        barslist[0].classList.add("dec-size");
        barslist[1].classList.add("dec-size");
        barslist[2].classList.add("dec-size");
        barslist[3].classList.add("inc-size");

        console.log(classnames3);
    }

}



function scroll_section(section){
    // console.log(section);
    $(document).ready(function() { 
        document.location.href='#'.concat(section);
    });
}

function down_scroll_click(){
    $('html, body').animate({scrollTop: $(document).height()}, 'slow');
    return false;
}



