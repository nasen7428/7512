function NodeView(viewid){
    var view=document.getElementById(viewid);
    this.btnaddbefor=view.getElementByClassName("viewnode-addbefor");
    this.btnaddafter=view.getElementByClassName("viewnode-addafter");
    this.devinfo=view.getElementByClassName"viewnode-info"
    this._edit=function(isshow){
        console.log("nodeview edit");
        if(isshow){
            this.btnaddbefor.show();
            this.btnaddafter.show();
        }else{
            this.btnaddbefor.hide();
            this.btnaddafter.hide();
        }
    }

}