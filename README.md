
# Stock Vol Prediction
### This project is mainly about predict short-term vol for stocks
### In the project, I used 100 stocks which are randomly select from SP500
### Models used: Garch(1,1), Random Forest, Recurrent NN
### Python ver: 3.6
### Package used: pandas, numpy, sklearn, keras, bokeh, quandl
### I also used a previous module created by myself to do the data collection part
# Result:


```python
import pandas as pd
from bokeh.io import output_notebook
import numpy as np
output_notebook()
```



    <div class="bk-root">
        <a href="http://bokeh.pydata.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
        <span id="614f6acc-fadd-44df-949e-199038503cb9">Loading BokehJS ...</span>
    </div>





```python
success = pd.read_csv('sucess_list.csv',index_col=0)
result = pd.read_csv('result.csv',index_col=0)
result = result.set_index(success['success'])
result = result[((result<0).sum(axis=1))==0]
```


```python
data = dict(RNN = list(result['RNN']),
            GARCH = list(result['garch']),
            RandomForest = list(result['random forest']))
from bokeh.charts import Area,defaults,show
defaults.width = 800
defaults.height = 400
area = Area(data,title='Stacked Area Chart for r-square',
            ylabel='r-square',legend='bottom_left')
area.xaxis.visible=False
show(area)
```




    <div class="bk-root">
        <div class="bk-plotdiv" id="0ed18411-ba96-427b-a181-786054bc7127"></div>
    </div>
<script type="text/javascript">
  
  (function(global) {
    function now() {
      return new Date();
    }
  
    var force = false;
  
    if (typeof (window._bokeh_onload_callbacks) === "undefined" || force === true) {
      window._bokeh_onload_callbacks = [];
      window._bokeh_is_loading = undefined;
    }
  
  
    
    if (typeof (window._bokeh_timeout) === "undefined" || force === true) {
      window._bokeh_timeout = Date.now() + 0;
      window._bokeh_failed_load = false;
    }
  
    var NB_LOAD_WARNING = {'data': {'text/html':
       "<div style='background-color: #fdd'>\n"+
       "<p>\n"+
       "BokehJS does not appear to have successfully loaded. If loading BokehJS from CDN, this \n"+
       "may be due to a slow or bad network connection. Possible fixes:\n"+
       "</p>\n"+
       "<ul>\n"+
       "<li>re-rerun `output_notebook()` to attempt to load from CDN again, or</li>\n"+
       "<li>use INLINE resources instead, as so:</li>\n"+
       "</ul>\n"+
       "<code>\n"+
       "from bokeh.resources import INLINE\n"+
       "output_notebook(resources=INLINE)\n"+
       "</code>\n"+
       "</div>"}};
  
    function display_loaded() {
      if (window.Bokeh !== undefined) {
        document.getElementById("0ed18411-ba96-427b-a181-786054bc7127").textContent = "BokehJS successfully loaded.";
      } else if (Date.now() < window._bokeh_timeout) {
        setTimeout(display_loaded, 100)
      }
    }
  
    function run_callbacks() {
      window._bokeh_onload_callbacks.forEach(function(callback) { callback() });
      delete window._bokeh_onload_callbacks
      console.info("Bokeh: all callbacks have finished");
    }
  
    function load_libs(js_urls, callback) {
      window._bokeh_onload_callbacks.push(callback);
      if (window._bokeh_is_loading > 0) {
        console.log("Bokeh: BokehJS is being loaded, scheduling callback at", now());
        return null;
      }
      if (js_urls == null || js_urls.length === 0) {
        run_callbacks();
        return null;
      }
      console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
      window._bokeh_is_loading = js_urls.length;
      for (var i = 0; i < js_urls.length; i++) {
        var url = js_urls[i];
        var s = document.createElement('script');
        s.src = url;
        s.async = false;
        s.onreadystatechange = s.onload = function() {
          window._bokeh_is_loading--;
          if (window._bokeh_is_loading === 0) {
            console.log("Bokeh: all BokehJS libraries loaded");
            run_callbacks()
          }
        };
        s.onerror = function() {
          console.warn("failed to load library " + url);
        };
        console.log("Bokeh: injecting script tag for BokehJS library: ", url);
        document.getElementsByTagName("head")[0].appendChild(s);
      }
    };var element = document.getElementById("0ed18411-ba96-427b-a181-786054bc7127");
    if (element == null) {
      console.log("Bokeh: ERROR: autoload.js configured with elementid '0ed18411-ba96-427b-a181-786054bc7127' but no matching script tag was found. ")
      return false;
    }
  
    var js_urls = [];
  
    var inline_js = [
      function(Bokeh) {
        (function() {
          var fn = function() {
            var docs_json = {"57299c32-28f1-4281-8cb7-e1606cfce072":{"roots":{"references":[{"attributes":{},"id":"bffe7f02-6e26-42a4-ab8d-330e98928bda","type":"BasicTickFormatter"},{"attributes":{"fill_alpha":{"value":0.8},"fill_color":{"value":"#5ab738"},"line_color":{"value":"#5ab738"},"xs":{"field":"x_values"},"ys":{"field":"y_values"}},"id":"abf59d59-86c2-4db9-9caf-5d5b0b846018","type":"Patches"},{"attributes":{"data_source":{"id":"b0813330-0f32-4c24-b0f0-c2f3b1fad540","type":"ColumnDataSource"},"glyph":{"id":"abf59d59-86c2-4db9-9caf-5d5b0b846018","type":"Patches"},"hover_glyph":null,"nonselection_glyph":null,"selection_glyph":null},"id":"a3db6696-5b49-45db-927e-b2b8646b8139","type":"GlyphRenderer"},{"attributes":{"plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"},"ticker":{"id":"f08602a1-193b-400a-bc32-eb5779083744","type":"BasicTicker"}},"id":"8c2d8e05-bc25-4d80-bcf2-c8cc530ee5cf","type":"Grid"},{"attributes":{"below":[{"id":"56d04efd-b3a6-44d9-8a7d-4a821e907cb9","type":"LinearAxis"}],"css_classes":null,"height":400,"left":[{"id":"d2abb715-03cb-4689-9306-20dd052f215f","type":"LinearAxis"}],"renderers":[{"id":"f129188e-ead7-4a1f-bd27-7e16910362a3","type":"BoxAnnotation"},{"id":"3228fb0a-d860-4fdb-b180-9fc59f2dca05","type":"GlyphRenderer"},{"id":"a3db6696-5b49-45db-927e-b2b8646b8139","type":"GlyphRenderer"},{"id":"12fcf69a-8c5d-4c8e-80ad-c7df592c0db7","type":"GlyphRenderer"},{"id":"521086ba-8b75-4b5d-b5c1-c5e5e6ce6ac4","type":"Legend"},{"id":"56d04efd-b3a6-44d9-8a7d-4a821e907cb9","type":"LinearAxis"},{"id":"d2abb715-03cb-4689-9306-20dd052f215f","type":"LinearAxis"},{"id":"8c2d8e05-bc25-4d80-bcf2-c8cc530ee5cf","type":"Grid"},{"id":"8aed3ac6-7c5c-494e-86de-3761be8f0efc","type":"Grid"}],"title":{"id":"56ca0cee-f470-44aa-88d2-419960644f23","type":"Title"},"tool_events":{"id":"2e9f9fba-39b0-4b17-bbdb-eb3f8b6253c7","type":"ToolEvents"},"toolbar":{"id":"a15125d1-efcc-4439-8afb-4c1a70d9942a","type":"Toolbar"},"width":800,"x_mapper_type":"auto","x_range":{"id":"2a3ecdc4-a2c2-4360-b6f4-9846e4589c8d","type":"Range1d"},"y_mapper_type":"auto","y_range":{"id":"18ab5477-a3ad-4158-b7eb-9c5e764d889b","type":"Range1d"}},"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"},{"attributes":{},"id":"dd281a9a-cb4e-420b-ad5f-c0234156f947","type":"BasicTicker"},{"attributes":{},"id":"2e9f9fba-39b0-4b17-bbdb-eb3f8b6253c7","type":"ToolEvents"},{"attributes":{"dimension":1,"plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"},"ticker":{"id":"dd281a9a-cb4e-420b-ad5f-c0234156f947","type":"BasicTicker"}},"id":"8aed3ac6-7c5c-494e-86de-3761be8f0efc","type":"Grid"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"f129188e-ead7-4a1f-bd27-7e16910362a3","type":"BoxAnnotation"},{"attributes":{"plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"}},"id":"e4daf316-d063-4c40-87bd-131c9cfda44e","type":"PanTool"},{"attributes":{"callback":null,"column_names":["x_values","y_values"],"data":{"chart_index":[{"series":"RNN"}],"series":["RNN"],"x_values":[[0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,99]],"y_values":[{"__ndarray__":"AAAAAAAAAACiDaqn7xbqP9uN/5KBmO4/p2EH0Y307D+v1amutX3sP55W/Gbnq+c/yGv9Qe4T7D9PoG+HGxLpP+frCqrsFO0/fzrtaEEV6z8yOT9h9wHtP4HhFQQM3uc/Pz1VE4nm7T+ZDBBurznrP7BC4kPkuOs/2mZz8pcN7D8eEpUFmAzsPz9fYyyUS+g/9GngaQlf7j/xw+cyp53rP113hKMXXuw/rMWEWuZn7D+u+sr7bxXjP4Z3zIxgAes/ukO8HiZY7D8+cbsS7ADtP+XcAsvbhOc/rs1BJmIZ7T8HiQOaF6rsP9/G7BcUh+4/h1RudhQD7j/PoMdwO8TrP57lcJg1H+0/POUJXbu05z+E/ytWkffpPzqmP1KjR+s/3ggpNnpZ6z+05RkiHPbrP7bzoYMdZew/+GKYcuki6j97JScj5SnsPwgCVLHTge0/bMA5kksl7j8ywJAxz6XRP3iXQvVhBuo/reguBiB26j+/CQIj+aTrP9qr0PaSe+w/wLwL0ukD7T8EX2LhYM7tPxV3pKTEles/UcHqQIMwqj8WOod5a4TrP6B3N8mDHuo/Vd8ZNgyg7T/8C6QwfIDrP6QeVSezeOk/rha0f9a07T9L5+IroBXsPyW+kJS3d+s/2ypeg70z7T/WYt94v8zrP0lB9F4co+0/Gr7Cm6yK6z/MfmlQ8OnrP0sk/B2Eluo/fm1akqdy5j/u3TRMntTtPy9CLr42SOs/OuxxQ8Vj6z+wGvHk997rP4KEzT7G6Oo/ETQ8hXKz6j8I+sIdu+nmP+MYgdwabuY/gxBCDAtf6j+IvMTdkJDrP6Sw7YxAQ+Q/qpzKaGId6z+eF+pZLuPtP2MENtEPHOo/XIx+P4el6z+rS1NyX0PpP765yb2HBe0/1o6eV4aN6D+dv9dJXpjOP+xev9tC1es/rl390CeQ7T8XoGneT53rP9KPfevFruw/5V7Ae/Ti6D8+9aSzgyftPyxh2rvvt+4/fbsb+mWw6j9FfaFaDfnqPx1L9Fhsgu0/iCImnfqt6z/Kx7qKyBDsP2PddE3n/+s/AugNpJnv6z+Cm2mp2eXoPwAAAAAAAAAA","dtype":"float64","shape":[102]}]}},"id":"b0813330-0f32-4c24-b0f0-c2f3b1fad540","type":"ColumnDataSource"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"e4daf316-d063-4c40-87bd-131c9cfda44e","type":"PanTool"},{"id":"6ca54304-874a-449a-9546-c3f4f06f1ed4","type":"WheelZoomTool"},{"id":"7e000336-62f2-4456-b976-7af256ed6c49","type":"BoxZoomTool"},{"id":"cd6f4a0e-0295-4775-8470-b332ab3a89fa","type":"SaveTool"},{"id":"6a5037f5-fcda-4ede-b1f9-b0cad2ac00e4","type":"ResetTool"},{"id":"3dd89c84-68a5-4798-8f1d-42a982b2c1e3","type":"HelpTool"}]},"id":"a15125d1-efcc-4439-8afb-4c1a70d9942a","type":"Toolbar"},{"attributes":{"plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"}},"id":"6ca54304-874a-449a-9546-c3f4f06f1ed4","type":"WheelZoomTool"},{"attributes":{"overlay":{"id":"f129188e-ead7-4a1f-bd27-7e16910362a3","type":"BoxAnnotation"},"plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"}},"id":"7e000336-62f2-4456-b976-7af256ed6c49","type":"BoxZoomTool"},{"attributes":{"plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"}},"id":"cd6f4a0e-0295-4775-8470-b332ab3a89fa","type":"SaveTool"},{"attributes":{"fill_alpha":{"value":0.8},"fill_color":{"value":"#407ee7"},"line_color":{"value":"#407ee7"},"xs":{"field":"x_values"},"ys":{"field":"y_values"}},"id":"29a572d8-0602-44f8-8c70-daa08f7973ca","type":"Patches"},{"attributes":{"data_source":{"id":"c45576cc-b201-4d6c-b90f-d326d5721166","type":"ColumnDataSource"},"glyph":{"id":"29a572d8-0602-44f8-8c70-daa08f7973ca","type":"Patches"},"hover_glyph":null,"nonselection_glyph":null,"selection_glyph":null},"id":"12fcf69a-8c5d-4c8e-80ad-c7df592c0db7","type":"GlyphRenderer"},{"attributes":{"plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"}},"id":"6a5037f5-fcda-4ede-b1f9-b0cad2ac00e4","type":"ResetTool"},{"attributes":{"plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"}},"id":"3dd89c84-68a5-4798-8f1d-42a982b2c1e3","type":"HelpTool"},{"attributes":{"items":[{"id":"2f9ec224-5ff6-470b-9588-5a16c01eb4d8","type":"LegendItem"},{"id":"3934fd1b-a00f-4402-9ce0-48e3efca5968","type":"LegendItem"},{"id":"24e7e0fc-b20c-485d-9c09-7fca90e5965f","type":"LegendItem"}],"location":"bottom_left","plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"}},"id":"521086ba-8b75-4b5d-b5c1-c5e5e6ce6ac4","type":"Legend"},{"attributes":{"callback":null,"end":1.0860298476188488,"start":-0.09872998614716809},"id":"18ab5477-a3ad-4158-b7eb-9c5e764d889b","type":"Range1d"},{"attributes":{"label":{"value":"RNN"},"renderers":[{"id":"a3db6696-5b49-45db-927e-b2b8646b8139","type":"GlyphRenderer"}]},"id":"3934fd1b-a00f-4402-9ce0-48e3efca5968","type":"LegendItem"},{"attributes":{"axis_label":"index","formatter":{"id":"ea77d0a8-4ace-43ad-aaa8-ad365f6c3099","type":"BasicTickFormatter"},"plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"},"ticker":{"id":"f08602a1-193b-400a-bc32-eb5779083744","type":"BasicTicker"},"visible":false},"id":"56d04efd-b3a6-44d9-8a7d-4a821e907cb9","type":"LinearAxis"},{"attributes":{"label":{"value":"GARCH"},"renderers":[{"id":"3228fb0a-d860-4fdb-b180-9fc59f2dca05","type":"GlyphRenderer"}]},"id":"2f9ec224-5ff6-470b-9588-5a16c01eb4d8","type":"LegendItem"},{"attributes":{},"id":"f08602a1-193b-400a-bc32-eb5779083744","type":"BasicTicker"},{"attributes":{},"id":"ea77d0a8-4ace-43ad-aaa8-ad365f6c3099","type":"BasicTickFormatter"},{"attributes":{"plot":null,"text":"Stacked Area Chart for r-square"},"id":"56ca0cee-f470-44aa-88d2-419960644f23","type":"Title"},{"attributes":{"callback":null,"end":108.9,"start":-9.9},"id":"2a3ecdc4-a2c2-4360-b6f4-9846e4589c8d","type":"Range1d"},{"attributes":{"axis_label":"r-square","formatter":{"id":"bffe7f02-6e26-42a4-ab8d-330e98928bda","type":"BasicTickFormatter"},"plot":{"id":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07","subtype":"Chart","type":"Plot"},"ticker":{"id":"dd281a9a-cb4e-420b-ad5f-c0234156f947","type":"BasicTicker"}},"id":"d2abb715-03cb-4689-9306-20dd052f215f","type":"LinearAxis"},{"attributes":{"fill_alpha":{"value":0.8},"fill_color":{"value":"#f22c40"},"line_color":{"value":"#f22c40"},"xs":{"field":"x_values"},"ys":{"field":"y_values"}},"id":"e9b905bc-70de-447e-a04a-a32886e539f8","type":"Patches"},{"attributes":{"callback":null,"column_names":["x_values","y_values"],"data":{"chart_index":[{"series":"RandomForest"}],"series":["RandomForest"],"x_values":[[0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,99]],"y_values":[{"__ndarray__":"AAAAAAAAAACWErJZBGrtPzL8YzwFruw/WNL5Wvrw7T8IJ0vVBQDtP/MNtB4GQuw/1PbQrIe57T/02ZYCBbnlP9AqN38wo+0/ycTLkzQO6z8zSddX2Y3tPxucOQS6Bes/64NZ7+907j/Z9T90pV/sP+sll7ALNOw/YpqyXoSU7D8q07Yl4Q/uP7CX3iDjm+s/hK/Nw/Vr7z+OGgiE3knuP6Up9pee6O0/4YQMGJMd7j+Fy6H8o8bmP1hlrW1UAu0/3uFh9yg77T/e5VKzf2DuP4QaPbnUy+o/M+yfxksf7j+N/a2TFtHtP58cugdvC+8/HwARv8DK7j/vj4LwUKHuP5VQ7xtFmu0/ai58MZS96z+rhPsNUC/tP6KrfTiBFus/AFKlzU1F7D+DC14V3NnsPykKq601ge0/KS1lp7cj7D/TI0gKfGXtPzBE4eEnTe4/RvrNdQ9f7j9LKf9WnErpP1jFC6XuFO0/GB06qglQ7T/jasewLqrsP7+kEdn3QO0/k3Kwvqcm7j/YZUWuP3nuP7VkwaoRnOw/9YxJeyLP3j/IaFsi537uPykvaEgQEu4/4O3luz0s7j/BWNTVBcbtP4ZF7XOdIu0/Fq4vfSLK7T9g7LRcVj/tP0NLZXK34+w/8Hj06FIk7j/CVOv51wftPzHmSPIiSO4/KY0x8RLg7T9Y6Epfmz3sPyLkY3nVvuw/m0+OPwBf6z8TyDKfaXTuP01d8bT4Je4/8ChTD7Oi7T80DABfte3tP3W6hzcKle0/9k+sZCYK6z8Irzb8FMnrPyi1uJ7AeOc/d9JwZEou7T9EuX8OZTPtP7981E+ZJOc/+LPEXD2X7D9Z2wCHCUHtP7JxNmAx3ew/aAIq6yQr7T++MiFJxgvsP29RJadpdu4/gRztjY4i7D+YK4hbM3zcP5WI5Y6dpOw/ENCuyZ4x7j882fwNjHjuP+Rvn5FrYu0/HNkXgryH7D/m4kYc81PuP9MMSKuf++4/zWv8oEFr6j9GOuIGk8ntP/5IhNIhhu0/avV9zHdY7T9cZrqiBCnsP7GZgb1nze0/tm4bn8YY7T+7FcNvmk7sPwAAAAAAAAAA","dtype":"float64","shape":[102]}]}},"id":"c45576cc-b201-4d6c-b90f-d326d5721166","type":"ColumnDataSource"},{"attributes":{"data_source":{"id":"e56a2b76-4972-418b-8403-f99d333dd36f","type":"ColumnDataSource"},"glyph":{"id":"e9b905bc-70de-447e-a04a-a32886e539f8","type":"Patches"},"hover_glyph":null,"nonselection_glyph":null,"selection_glyph":null},"id":"3228fb0a-d860-4fdb-b180-9fc59f2dca05","type":"GlyphRenderer"},{"attributes":{"label":{"value":"RandomForest"},"renderers":[{"id":"12fcf69a-8c5d-4c8e-80ad-c7df592c0db7","type":"GlyphRenderer"}]},"id":"24e7e0fc-b20c-485d-9c09-7fca90e5965f","type":"LegendItem"},{"attributes":{"callback":null,"column_names":["x_values","y_values"],"data":{"chart_index":[{"series":"GARCH"}],"series":["GARCH"],"x_values":[[0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,99]],"y_values":[{"__ndarray__":"AAAAAAAAAADbxKPLi8zuP4shDwPaNO8/r6JTgfJ97z+saQFF9N7tP0ETBOghZO8/vCs5x2Fw7z+yNjyEoT3vP0JRuAhYDO8/mK4uG97C7j+jRaOjNvXuP1Wldv6oOO8/wPwjSHD17j/VE2blZAbvPzyqiVH5w+4/NW110mcO7z/1sYzeQTTvP+wX5vOGDO8/qG0tYyCB7z9QEEJxqnDvP0803f4XJ+8/ze9OUZ1H7z/Y2PnBlo/vP6B+dDgEN+8/HprIkk3w7T+DtA2/C13vP+upUl6cBO8/4m2m82Zk7z8HmDJX2zLvP6519t77gO8/EKUusK9w7z/98QzXrHTvP7fuALw4eO8/V0Wb5sy67j9jrr0V8CfvP/jiK0OKbu4/iYOV1lkV7z9LVouSnm3vP/vFxbKa3+4/IuVsXWIt7z8hdr8YF5HvP3BryHqiae8/8vvCg/tM7z/TFI+grTvtPxIUqurON+8/cy1WUOZs7j8GPQhq4RvvP3HFgs/KWu8/7vVX/pY47z+AK+RceGnvP4j4RQ1Ri+8/DgGANE9u7z/k0QCTw2/vP5FN2EuIUO8//ouzADdP7z9Ns5x59tjuP7TCl+prRO8/ZOPnN7Vi7z9fbKbJs9zuP76RoAED7+4/4hg9OZXF7j9urXKadWDuP6T1ag2KZu8/Qb7Kz6hI7z8jDZR+Wz7vPxNrYs8Hg+8/BmOtfAuC7j8S/B078ZXvP8yZH5FqA+8/r62pN/k17z9xWUFTImnvP6lJTwA9Re8/WWmZh0B17z+0FTvPh1nvP1F3jKmo0O4/EzQ8fVNo7z/5f7FFdxvvPwrMB7pDye4/LniTp8gO7z8JIQj4TdPuP0O/VlzdXu8/Yp7f/Fzn7j+jOySpI2DuP8Uydh4pLO8/x8jZJcZj7z/HvsW7UgzuP+MJoeGWOe8/kiEJYatB7z/bELSETB/uP4y6nHJFgO8/y9iBcpAc7z+gW2ElmrvuPwHQnaINXO8/faEakRX/7j/otwvh9ZfvP9XuRdsYSu8/eQaulKj67j/vzkdphRPvP4Hf3wvbTu8/wShEmeDP7j8NH9aOON3uPwAAAAAAAAAA","dtype":"float64","shape":[102]}]}},"id":"e56a2b76-4972-418b-8403-f99d333dd36f","type":"ColumnDataSource"}],"root_ids":["f8d47c47-073d-4a27-bdfc-d5f80cbc9c07"]},"title":"Bokeh Application","version":"0.12.4"}};
            var render_items = [{"docid":"57299c32-28f1-4281-8cb7-e1606cfce072","elementid":"0ed18411-ba96-427b-a181-786054bc7127","modelid":"f8d47c47-073d-4a27-bdfc-d5f80cbc9c07"}];
            
            Bokeh.embed.embed_items(docs_json, render_items);
          };
          if (document.readyState != "loading") fn();
          else document.addEventListener("DOMContentLoaded", fn);
        })();
      },
      function(Bokeh) {
      }
    ];
  
    function run_inline_js() {
      
      if ((window.Bokeh !== undefined) || (force === true)) {
        for (var i = 0; i < inline_js.length; i++) {
          inline_js[i](window.Bokeh);
        }if (force === true) {
          display_loaded();
        }} else if (Date.now() < window._bokeh_timeout) {
        setTimeout(run_inline_js, 100);
      } else if (!window._bokeh_failed_load) {
        console.log("Bokeh: BokehJS failed to load within specified timeout.");
        window._bokeh_failed_load = true;
      } else if (force !== true) {
        var cell = $(document.getElementById("0ed18411-ba96-427b-a181-786054bc7127")).parents('.cell').data().cell;
        cell.output_area.append_execute_result(NB_LOAD_WARNING)
      }
  
    }
  
    if (window._bokeh_is_loading === 0) {
      console.log("Bokeh: BokehJS loaded, going straight to plotting");
      run_inline_js();
    } else {
      load_libs(js_urls, function() {
        console.log("Bokeh: BokehJS plotting callback run at", now());
        run_inline_js();
      });
    }
  }(this));
</script>


## We can conclude that for short term vol prediction:
- Garch(1,1) has higher r-square and is more stable than the other two
- RNN has the worst performance, it may be due to the limited number of observations in the dataset, from the log when models were running , we can see the initialization has a huge impact on the final result for RNN
