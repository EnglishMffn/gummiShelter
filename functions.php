<?php

// Include Divi original theme
// function my_theme_enqueue_styles() { 
//     wp_enqueue_style( 'parent-style', get_template_directory_uri() . '/style.css' );
// }
// add_action( 'wp_enqueue_scripts', 'my_theme_enqueue_styles' );


// Remove JQuery and other bloat
add_filter( 'wp_enqueue_scripts', 'remove_the_bloat', PHP_INT_MAX );

function remove_the_bloat( ){
    wp_dequeue_script( 'jquery');
    wp_deregister_script( 'jquery');   
    wp_deregister_script( 'wp-embed');
    wp_deregister_style( 'dashicons' );
    wp_deregister_style( 'jetpack' );
    wp_dequeue_style( 'wp-block-library' );
}