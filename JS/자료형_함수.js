function add(x,y){
	return x+y;
}
function sub(x,y){
	return x-y;
}
function mul(x,y){
	return x*y;
}
function div(x,y){
	return x/y;
}

function push(f) {
	//n1과 n2의 값을 가지고 오겠다
	n1Value = $('#n1').val();
	n2Value = $('#n2').val();
	n1 = parseInt(n1Value);
	n2 = parseInt(n2Value);
	alert(f(n1,n2));
}

//body부분을 먼저 RAM에 읽어들인 후 -> jquery 실행되도록
$(function() { //"body가 준비되면"이라는 뜻 js의 document.ready
	
	//버튼을 클릭했을 때 
	$('#b1').click(function() {
		push(add);
	})
	$('#b2').click(function() {
		push(sub);
	})
	$('#b3').click(function() {
		push(mul);
	})
	$('#b4').click(function() {
		push(div);
	})
})	
