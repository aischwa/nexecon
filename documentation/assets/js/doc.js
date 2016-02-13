$(function(){
    
    /*---------------------------------------*/
    /*  JQUERY FOR PAGE SCROLLING FEATURE
    /*  requires jQuery Easing plugin
    /*---------------------------------------*/
    var pageScroll = function(){
        $('.page-scroll a').bind('click', function(e){
            e.preventDefault();

            var $anchor = $(this);

            var offset = $('body').attr('data-offset');
            
            if($('.navbar.navbar-fixed-top').hasClass('side-menu') && $(window).width() >= 992){
                $('body').data('offset', 1);
                offset = $('body').data('offset');
            }

            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - (offset - 1)
            }, 1500, 'easeInOutExpo');
        });
    };
    
    
    /*---------------------------------------*/
    /*  STICKY NAVBAR
    /*---------------------------------------*/
    $('.navbar.navbar-fixed-top').sticky({topSpacing: 0});
    
    var stickySideMenu = function(){
        var navbar = $('.navbar.navbar-fixed-top.side-menu');
        
        if ($(window).width() >= 992) {        
            navbar.unstick();
        }
        else
        {
            navbar.unstick();
            navbar.sticky({topSpacing: 0});
        }
    };
    
    pageScroll();
    stickySideMenu();
    
    $(window).smartresize(function(){
        pageScroll();
        stickySideMenu();
    });
    
    $('.navbar-trigger-open').click(function(e) {
        e.preventDefault();
        $('.navbar.side-menu').toggleClass('active');
        $('body.push.push-left').toggleClass('pushed-left');
        $('body.push.push-right').toggleClass('pushed-right');
    });

    $('.navbar-trigger-close').click(function(e) {
        e.preventDefault();
        $('.navbar.side-menu').toggleClass('active');
        $('body.push.push-left').toggleClass('pushed-left');
        $('body.push.push-right').toggleClass('pushed-right');
    });
    
    
    /*---------------------------------------*/
    /*  MAKE CODE PREETY
    /*---------------------------------------*/
    window.prettyPrint && prettyPrint();
});