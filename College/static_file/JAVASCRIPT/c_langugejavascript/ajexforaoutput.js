 $(function() {
            function call_ajax(f) {
               // var answer=$('#answer').val();
               // var option=$('#option option:selected').val();
               var data=$('#text1').val();
               //data ={x:2};
               //console.log(data);
               data={'data':data,'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()};
                //console.log(data);
                $.ajax({
                    url: '/Clanguage';//"{% url 'C_language:c_compile' %}",//'/heart/pridict/',
                    data: data,
                    type: 'POST',
                    success: f,
                    error: function(error) {
                        //console.log(error);
                    }
                });
            }

           function server_response(response) {
                // convert to json format
               const r = JSON.parse(response);
              // console.log(r);
                
                // include the result in the dom
                // text.innerHTML = '<strong id="result">' + r.ans + '</strong>';
               
                
                  
                  if (r['error']!=null) {
                  var text = document.createElement("I");
                  text.innerHTML = '<strong id="result value="">'+'</strong>';
                  text.innerHTML = '<h3 style="color: red;">'+String(r['error'])+'</h3>' ; 
                  //console.log(text);
                  console.log(r)
               //console.log($('#result').replaceWith(text));
               $('#result').html(text);
              
               }

               else{
                  var text = document.createElement("I");
                  text.innerHTML = '<strong id="result value="">'+'</strong>';
                  text.innerHTML = '<h3 style="color: black;">'+r['output']+'</h3>' ; 
                  //console.log(text);
                  console.log(r)
                   $('#result').html(text);

               
              }
            }
              

            //Validate
            $('#form').submit(function(e) {
                e.preventDefault();
                call_ajax(server_response);
            });
        });