function color() {
        texto = document.getElementById("texto").value;
        if (texto=="azul"){
            document.getElementById("caja").style.backgroundColor = "blue";
        }
        else if (texto=="rojo"){
            document.getElementById("caja").style.backgroundColor = "red";
        }
        else if (texto=="amarillo"){
            document.getElementById("caja").style.backgroundColor = "yellow";
        }   
        else{
            document.getElementById("caja").style.backgroundColor = "white";
        }
    }