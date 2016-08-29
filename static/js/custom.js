(function ($) {
    "use strict";
    var mainApp = {
        main_fun: function () {
            /*====================================

             CUSTOM LINKS SCROLLING FUNCTION 
            ======================================*/
            $('a[href*=#]').click(function () {
                if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '')
               && location.hostname == this.hostname) {
                    var $target = $(this.hash);
                    $target = $target.length && $target
                    || $('[name=' + this.hash.slice(1) + ']');
                    if ($target.length) {
                        var targetOffset = $target.offset().top;
                        $('html,body')
                        .animate({ scrollTop: targetOffset }, 800); //set scroll speed here
                        return false;
                    }
                }
            });
            /*====================================

            VAGAS SLIDESHOW SCRIPTS

            ======================================*/
            $(function () {
                $.vegas('slideshow', {
                    backgrounds: [
                      //{ src: 'http://eaae-astronomy.org/blog/wp-content/uploads/2011/07/galaxy_spacewarp.jpg', fade: 1000, delay: 9000 },
                      //
                      //{ src: 'http://i.giflike.com/dakt2dQ.gif', fade: 1000, delay: 9000 }, 
                        { src: '/static/img/newtons_cradle.gif', fade: 1000, delay: Infinity }, 
                    ]
                })('overlay', {
                    /** SLIDESHOW OVERLAY IMAGE **/
                    src: '/static/plugins/vegas/overlays/15.png' // THERE ARE TOTAL 01 TO 15 .png IMAGES AT THE PATH GIVEN, WHICH YOU CAN USE HERE
                });
            });
            /*====================================

                NAV SCRIPTS

            ======================================*/
            $(window).bind('scroll', function () {
                var navHeight = $(window).height() -50;
                if ($(window).scrollTop() > navHeight) {
                    $('nav').addClass('fixed');
                }
                else {
                    $('nav').removeClass('fixed');
                }
            });
            /*====================================

               WRITE YOUR SCRIPTS BELOW 

           ======================================*/
        },
        initialization: function () {
            mainApp.main_fun();
        }
    }
    // Initializing ///
    $(document).ready(function () {
        mainApp.main_fun();
    });
}(jQuery));







