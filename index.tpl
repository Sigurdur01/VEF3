<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>HasarFréttir</title>
	<link rel="stylesheet" type="text/css" href="static/styles.css">
</head>
<body>
	%include('haus.tpl')
	<div class="row">
		<img src="static/Breakingnews.jpg">
		<section>{{ frett[0][0] }}</section>
		<section>New news</section>
		<section><img src="/static/Breakingnews0.jpg"></section>
		<section>fréttalisti</section>
			<ul>
				<li><a href="/frett/{{cnt}}">{{i[0]}}</a></li>
			</ul>
	</div>
	%include('footer.tpl')
</body>
</html>