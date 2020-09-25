<html>

<head>
    <title>محلل القرآن - Coran parser</title>

    <link rel="stylesheet" href="styles.css">

</head>

<body>

    <div class=header>
        <h1 class=titre>Coran parser - محلل القرآن</h1>
        <!-- <h2 class=titre> اللَّهُ نَزَّلَ أَحسَنَ الحَديثِ كِتٰبًا مُتَشٰبِهًا مَثانِىَ تَقشَعِرُّ مِنهُ جُلودُ الَّذينَ يَخشَونَ رَبَّهُم ثُمَّ تَلينُ جُلودُهُم وَقُلوبُهُم إِلىٰ ذِكرِ اللَّهِ ذٰلِكَ هُدَى اللَّهِ يَهدى بِهِ مَن يَشاءُ وَمَن يُضلِلِ اللَّهُ فَما لَهُ مِن هادٍ </h2> -->
        <div class=marquee-rtl>
            <div>Find something easily in the coran</div>
        </div>
    </div>
    <img class=logo_grand src='coran_fond_transp.png' ></br>
    <!-- Group of buttons-->
    <form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post">
        <!-- Button app python -->
        <!-- <input class=button type="submit" id="coran_browser" name="coran_browser" value="Coran Browser">  -->
        <!-- Button read coran -->
        <input class=button type="submit" id="read_coran" name="read_coran" value="Show all coran">
        <!-- Button count weight -->
        <input class=button type="submit" id="count_words" name="count_words" value="Count words">
        
        <!-- Button find sourate -->
        <input class=button type="submit" id="sourate" name="sourate" value="Find Sourate num">
        <input class=num_sourate type="text" id="num_sourate" name="num_sourate" value="1">
        <!-- Button find word or sentence in the coran -->
        <input class=button type="submit" id="find_words" name="find_words" value="Find word in coran">
        <input class=word_to_find type="text" id="word" name="word" placeholder="example : اللَّه">
    </form>

    <div class=parchemin>
        <div class=text_parchemin>
            <?php

            ## including the file of coran
            #include 'quran-uthmani-min.txt';

            ## FunctionRead and print the coran text 
            function read_coran(){
                $fh = fopen('quran-uthmani-min.txt', 'r');
                $result = '';
                $style = '<div style="padding:15%;overflow:hidden;">';
                while(!feof($fh)){
                    $line = fgets($fh);
                    $line_splits = explode("|",$line);
                    
                    
                    $result = $result.'<div style="font-size:0.85em;color:green">Sourate: '.$line_splits[0].'   Ayyat: '.$line_splits[1].'</div> <div style="font-size:1.55em;color:#0e3c68;font-weight:bold;">'.$line_splits[2].'</div></br>';

                }
                echo $style.$result;
            }

            ## Function search sourate 
            function sourate($num_sourate){
                $fh = fopen('quran-uthmani-min.txt', 'r');
                $result ='';
                $title = '<div style="font-size:1.55em;color:blue;font-weight:bold;">Sourate '.$num_sourate.'</div></br></br>';

                while(!feof($fh)){
                    $line =fgets($fh);
                    $line_splits = explode("|",$line);
                    #echo $num_sourate; echo "<------->"; echo $line_splits[0];  echo '<br/>';
                    if(strcmp($line_splits[0],$num_sourate)==0){
                        $result = $result.'<div style="font-size:0.85em;color:green">Sourate: '.$line_splits[0].'   Ayyat: '.$line_splits[1].'</div> <div style="font-size:1.55em;color:#0e3c68;font-weight:bold;">'.$line_splits[2].'</div></br>';
                    }
                }
                $result = $title.$result;
                $style = '<div style="padding:15%;overflow:hidden;">';
                echo $style.$result.'</div>';
            }

            ## Finction search word in the coran
            function find_word($word){
                $fh = fopen('quran-uthmani-min.txt', 'r');
                $result ='';
                $number=0;
                while(!feof($fh)){
                    $line =fgets($fh);
                    $line_splits = explode("|",$line);
                    if(strstr($line_splits[2],$word)){
                        $result = $result.'<div style="font-size:0.85em;color:green">Sourate: '.$line_splits[0].'   Ayyat: '.$line_splits[1].'</div> <div style="font-size:1.55em;color:#0e3c68;font-weight:bold;">'.$line_splits[2].'</div></br>';
                        $number = $number + substr_count($line_splits[2],$word);
                    }
                }
                $title = '<div style="font-size:1.55em;color:red;font-weight:bold">Total of '.$word.' in the coran is : '.$number.'</div></br>';
                $style = '<div style="padding:15%;overflow:hidden;position:relative;">';
                echo $style.$title.$result.'</div>';

            }
            
            ## Function compte words of coran
            function count_words(){
                $fh = fopen('quran-uthmani-min.txt', 'r');
                $result ='';
                $number=0;
                $style = '<div style="padding:15%;overflow:hidden;position:relative;">';
                
                while(!feof($fh)){
                    $line =fgets($fh);
                    $line_splits = explode("|",$line);
                    $words_splits = explode(" ",$line_splits[2]);
                    $number = $number + sizeof($words_splits);
                    echo $style.$line_splits[2].sizeof($words_splits).'</div>';
                }
                
                $title = '<div style="font-size:1.55em;color:red;font-weight:bold">Total of words  in the coran is : '.$number.'</div></br>';
                echo $style.$title.'</div>';


            }
            
            ## Function count weight of char in the coran
            function count_weight(){
                $fh = fopen('quran-uthmani-min.txt', 'r');
                $result ='';
                while (false !== ($char = fgets($fh))) {

                    echo $style.$char.'</br></div>';
                }
            }


            ## Run python application
            if(!empty($_POST['coran_browser'])){
                ## Run the coran browser
                $command = escapeshellcmd('python /Users/amadouourybah/Desktop/My_coran_project/deep_learning_coran.py');
                $output = shell_exec($command);
                echo $output;
            }

            ## Call read_coran function 
            if(!empty($_POST['read_coran'])){
                read_coran();
            }

            ## Find sourate
            if(!empty($_POST['sourate'])){
                sourate($_POST['num_sourate']);
            }

            ## Find Word in the coran
            if(!empty($_POST['find_words'])){
                find_word($_POST['word']);
            }

            ## Count weight
            if(!empty($_POST['count_words'])){
                count_words();
            }

            ?>
        </div>
    </div>

    <div class=footer>
        <img class=logo src='coran.png'>
        <p>@Author: Bah Amadou Oury</p>
    </div>

</body>

</html>