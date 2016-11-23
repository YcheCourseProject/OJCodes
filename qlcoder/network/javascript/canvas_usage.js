/**
 * Created by cheyulin on 11/23/16.
 */
//清空页面
document.body.innerHTML = ""
//创建2iframe(加载题目和答题用)
a = document.createElement('iframe')
a.setAttribute('name', "a")
a.style.width = '48%'
a.style.height = '90%'
document.body.appendChild(a)
b = document.createElement('iframe')
b.setAttribute('name', "b")
b.style.width = '48%'
b.style.height = '90%'
document.body.appendChild(b)
//iframeA题目开始加载
a.src = location.href;
//题目加载完毕执行
a.onload = function () {
    //题目表单定向至iframeB
    a.contentWindow.document.getElementsByTagName('form')[0].setAttribute('target', 'b')


    //解题思路

    //添加canvas
    a.contentWindow.document.body.appendChild(document.createElement('canvas'))

    //获取canvas元素
    can1 = a.contentWindow.document.getElementsByTagName('canvas')[0]
    //获取canvas上下文
    ctx1 = can1.getContext('2d')
    //获取图片
    var img = a.contentWindow.document.getElementsByTagName("img")[0];
    //图片放至canvas
    ctx1.drawImage(img, 0, 0);
    //获取图片数据
    var imgdata = ctx1.getImageData(0, 0, 150, 30);
    //记录边框空白[上下左右]
    side = [30, 0, 150, 0]
    //i宽度,j高度,每个像素RGBA占4位
    for (i = 0; i < 150; i++) {
        for (j = 0; j < 30; j++) {
            if (imgdata.data[(j * 150 + i) * 4] > 20) {
                if (side[0] > j)side[0] = j
                if (side[1] < j)side[1] = j
                if (side[2] > i)side[2] = i
                if (side[3] < i)side[3] = i
            }
        }
    }
    //重绘图片draw(源,源图片左起始位置,源图片上起始位置,源图片宽度,源图片高度,放置左边位置,放置上边位置,放置宽度,放置高度)
    ctx1.drawImage(img, tag[2], tag[0], tag[3] - tag[2], tag[1] - tag[0], 0, 0, 150, 30);
    //记录图片每列上边距
    ch = []
    //获取大小统一后的图片数据
    imgdata = ctx1.getImageData(0, 0, 150, 30);
    for (i = 0; i < 150; i++) {
        ch.push(30)//默认距离上边为30像素
        for (j = 0; j < 30; j++) {
            if (imgdata.data[(j * 150 + i) * 4] > 20) {
                ch[i] = j;//如果遇到非黑像素,结束当前列处理
                break;
            }
            //顶部黑色转白色
            imgdata.data[(j * 150 + i) * 4] = 255;
            imgdata.data[(j * 150 + i) * 4 + 1] = 255;
            imgdata.data[(j * 150 + i) * 4 + 2] = 255;
            imgdata.data[(j * 150 + i) * 4 + 3] = 255;
        }
    }
    //放回图片,调试用
    ctx1.putImageData(imgdata, 0, 0);
    mini = -1//和标准图片差距
    minitag = ''//图片内容
    //预置数据
    data = {
        'pass': pass,
        'user': user,
        'phone': phone,
        'intro': intro,
        'email': email,
        'sex': sex,
        'birth': birth,
        'repass': repass
    }
    //寻找和记录差距最小的预置数据,记录标签
    for (tag in data) {
        ans = 0
        for (i = 0; i < 150; i++) {
            ans += Math.abs(ch[i] - data[tag][i])
        }
        if (mini == -1 || mini > ans) {
            mini = ans;
            minitag = tag;
        }
    }
    //设定提交数据
    a.contentWindow.document.getElementsByTagName("input")[pic].value = minitag

    //提交表单
    a.contentWindow.document.getElementsByTagName("input")[9].click();
}
//提交成功刷新a
b.onload = function () {
    a.src = location.href;
}