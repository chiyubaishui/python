1��CSS�������?
	1. ֱ��д�ڱ�ǩ���� style="��ʽ1;��ʽ2;"
	2. ��head��ͨ��style��ǩ����
	3. ����ʽ����д��css�ļ���,Ȼ����html�ļ���ͨ��link��ǩ����
��һ��
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>CSS����ʾ��</title>
    <!--<style>-->
        <!--p {-->
            <!--color: green;-->   
        <!--}-->
    <!--</style>-->
    <link rel="stylesheet" href="index.css">
</head>
<body>

<!--<p style="color: blue">����</p>-->
<p id="p1">����</p>
<p id="p2">����Ǹ���ɫ�ĺ���</p>
<p class="c1">����Ǹ���ɫ�ĺ���</p>
<p class="c1">����Ǹ���ɫ�ĺ���</p>
<p class="c1">����Ǹ���ɫ�ĺ���</p>
<p class="c1">����Ǹ���ɫ�ĺ���</p>
<h1>����</h1>

</body>
</html>

2��CSS�﷨  ѡ���� {��ʽ1;��ʽ2}
p {
    color: red;
    font-size: 18px
}


3��ע�ͣ�
/*��ǩѡ����*/

4��CSS���ұ�ǩ�ķ�ʽ(ѡ����)
1. ����ѡ����
	1. ��ǩѡ����     ������ ������\ͳһ\Ĭ�ϵ���ʽ
	2. IDѡ����       ������ ���ض���ǩ�����ض���ʽ
	3. ��ѡ����       ������ ��ĳһЩ��ǩ������ͬ����ʽ
/*��ǩѡ����*/
h1 {
    color: green;
}
/*IDѡ����*/
#p2 {
    color: black;
}
/*��ѡ����*/
.c1 {
    color: yellow;
}
2. ͨ��ѡ����
* {
  color: white;
}

3�����ѡ����
���ѡ����
/*li�ڲ���a��ǩ����������ɫ*/
li a {
  color: green;
}
����ѡ����
/*ѡ�����и����� <div> Ԫ�ص� <p> Ԫ��*/
div>p {
  font-family: "Arial Black", arial-black, cursive;
}
����ѡ����
/*ѡ�����н�����<div>Ԫ��֮���<p>Ԫ��*/
div+p {
  margin: 5px;
}
�ܵ�ѡ����
/*i1�������е��ֵ�p��ǩ*/
#i1~p {
  border: 2px solid royalblue;
}

4������ѡ����
/*����ѡȡ����ָ�����Ե�Ԫ�ء�*/
p[title] {
  color: red;
}
/*����ѡȡ����ָ�����Ժ�ֵ��Ԫ�ء�*/
p[title="213"] {
  color: green;
}
5�������Ƕ��
����
�����Ԫ�ص���ʽ��ͬ��ʱ������û�б�Ҫ�ظ���Ϊÿ��Ԫ�ض�������ʽ�����ǿ���ͨ���ڶ��ѡ����֮��ʹ�ö��ŷָ��ķ���ѡ������ͳһ����Ԫ����ʽ�� 

���磺
div, p {
  color: red;
}
����Ĵ���Ϊdiv��ǩ��p��ǩͳһ��������Ϊ��ɫ��

ͨ�������ǻ��������д��������:
div,
p {
  color: red;
}
Ƕ��
����ѡ�������Ի������ʹ�ã����磺.c1���ڲ�����p��ǩ����������ɫΪ��ɫ��

.c1 p {
  color: red;
}

6��α��ѡ����
/* δ���ʵ����� */
a:link {
  color: #FF0000
}

/* �ѷ��ʵ����� */
a:visited {
  color: #00FF00
} 

/* ����ƶ��������� */
a:hover {
  color: #FF00FF
} 

/* ѡ�������� */ 
a:active {
  color: #0000FF
}

/*input������ȡ����ʱ��ʽ*/
input:focus {
  outline: none;
  background-color: #eee;
}

7��αԪ��ѡ����
first-letter
���õĸ�����ĸ����������ʽ��

p:first-letter {
  font-size: 48px;
  color: red;
}
before
/*��ÿ��<p>Ԫ��֮ǰ��������*/
p:before {
  content:"*";
  color:red;
}
after
/*��ÿ��<p>Ԫ��֮���������*/
p:after {
  content:"[?]";
  color:blue;
} 
before��after�������������