package com.example.cat.a7512_android;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.GridLayout;
import com.example.cat.a7512_android.view.NodeView;

public class EditNodeSpace extends AppCompatActivity {

    GridLayout nodespace;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.edit_nodespace);
        nodespace= (GridLayout) findViewById(R.id.nodespace);
        findViewById(R.id.button_add_new_node).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                addNewNodeView();
            }
        });
    }

    private void addNewNodeView(){
        NodeView nodeView = new NodeView(this);
        nodespace.addView(nodeView);
    }
}

