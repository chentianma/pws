/**
 * Created by Ruby on 2016/9/27.
 */

$(document).ready(function () {
    var thisUrl = window.location.pathname;
    var navlist = $("#navList").children();
//        alert("thisUrl:" + thisUrl);
    var i;
    for (i = 0; i < navlist.length; i++) {
        var t = $("#navList li").eq(i).children("a").attr("href");
        // console.log(t);
        if (thisUrl === t) {
            $("#navList li").eq(i).attr("class", "active")
        }
    }
});