<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>HasarFréttir</title>
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
</head>
<body>
    % include('haus.tpl')
    <div class="row">
        <section><h3>{{frett[0]}}</h3></section>
        <section> <!--autt--></section>
        <section><img src="/static/panda{{nr}}.jpg"></section>
        <section class=pd2>
            <p>{{frett[1]}}</p>
            <p>höfundur:  {{frett[2]}}</p>
            <h5><a href="/b">Aftur á Hasarfréttir</a></h5>
        </section>
    </div>
    % include('footer.tpl')
</body>
</html>