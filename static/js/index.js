$(document).ready(function(){
	// 广告栏
	var mySwiper1 = new Swiper('#Banner-Swiper', {
		grabCursor: true, //鼠标抓手
		speed: 500, //滑入速度
		autoplay: {
			delay: 5000,
			disableOnInteraction: false,
			waitForTransition: false, //过渡完后才读秒
		}, //自动播放,延迟时间
		loop: true, //循环
		roundLengths: true,
		followFinger: false, //鼠标释放时才滑动
		preventInteractionOnTransition: true,
		navigation: {
			nextEl: '.rightarrow',
			prevEl: '.leftarrow',
		},
	});
	// 登录注册栏
	var mySwiper2 = new Swiper('#Login-swiper', {
		effect: 'flip',
		speed: 300, //滑入速度
		roundLengths: true,
		noSwiping : true,
		navigation: {
			nextEl: '#goRegister',
			prevEl: '#goLogin',
		},
	})
});


