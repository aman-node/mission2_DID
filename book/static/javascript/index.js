function updateClock() {
    var now = new Date();
    var dname = now.getDay(),
        month = now.getMonth(),
        dnum = now.getDate(),
        year = now.getFullYear(),
        hours = now.getHours(),
        minutes = now.getMinutes(),
        seconds = now.getSeconds(),
        period = "AM";
 
    if (hours == 0) {
        hours = 12;
    }
    if (hours > 12) {
        hours = hours - 12;
        period = "PM";
    }

    Number.prototype.pad = function (digits) {
        for (var n = this.toString(); n.length < digits; n = 0 + n);
        return n;
    }

    var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var ids = ['dayname', 'month', 'daynum', 'year', 'hour', 'minutes', 'seconds', 'period'];
    var values = [week[dname], months[month], dnum, year, hours.pad(2), minutes.pad(2), seconds.pad(2), period];
    for (var i = 0; i < ids.length; i++)
        document.getElementById(ids[i]).firstChild.nodeValue = values[i];
}

function initClock() {
    updateClock();
    window.setInterval(updateClock, 1000);

}

function moveRight(img, tit) {
    var img_old = document.getElementById("imgid").src;
    var tit_old = document.getElementById("title_id").innerText;
    if (img_old == img && tit_old == tit) {return;}

    
    $('#myimg').animate({ right: $(window).width()+$("#imgid").width()+"px" }, {
        easing: 'swing',
        complete: function () {
            $(".slidertext").fadeOut(200, function () {
                dispData(img, tit);
                $(".slidertext").fadeIn(200);
            });

        }
    }
    );
}
$(document).ready(function () {
    $("#myimg").css({ 'right': '', 'top': '-30px' });
    $("#myimg").animate({ top: '30px' });
    $(".imgcon").click(function () {
        var img = $(this).attr("src");
        var tit = $(this).data("title");

        console.log(tit)
        moveRight(img, tit);
    });
    
})



function dispData(img, tit) {
    const img1 = document.getElementById("imgid").src = img;
    const title = document.getElementById("title_id").innerText = tit;
    document.getElementById("imgid").onload = function () {

        $("#myimg").css({ 'right': '', 'top': '-30px' });
        $("#myimg").animate({ top: '30px' });
    }
}


