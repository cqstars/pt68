var svgNS = "http://www.w3.org/2000/svg"

//根据设置页面创建单元格
function creatCell() {

    jpeditorAttr.cells.length = 0;
    for (var i = 0; i < jpeditorAttr.height / jpeditorAttr.fontsize; i++) {
        for (var j = 0; j < parseInt(jpeditorAttr.width / jpeditorAttr.fontsize); j++) {
            new Cell(i, j, j * jpeditorAttr.fontsize, i * jpeditorAttr.fontsize);
        }
    }

}

//createTag(tag,objAttr)的核心思想就是获取需要创建的标签，创建对应的标签元素，然后遍历多个属性值objArr生成在标签元素中
function createTag(tag, objAttr) {
    var elem = document.createElementNS(svgNS, tag);
    for (var attr in objAttr) {
        elem.setAttribute(attr, objAttr[attr]);
    }
    return elem;
}

//创造复用的use标签
function CreatDefsUse(tag, objAttr) {
    let XLink_NS = 'http://www.w3.org/1999/xlink';
    let useelement = document.createElementNS(svgNS, 'use');
    useelement.setAttributeNS(XLink_NS, 'ink:href', tag);
    for (var attr in objAttr) {
        useelement.setAttribute(attr, objAttr[attr]);
    }
    return useelement;

}

function CreatDefs() {
    let t=createTag("text",{"x":0,"y":0,"font-size":jpeditorAttr.fontsize,"font-family":"Verdana"});
    //let XLink_NS = 'http://www.w3.org/1999/xlink';
    //let useelement = document.createElementNS(svgNS, 'g');
    t.innerHTML="7";
    document.getElementById("alto6").appendChild(t);
}