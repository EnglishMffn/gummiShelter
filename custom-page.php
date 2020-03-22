<?php 
/* Template Name: Eborall Custom Page */
// Brother Lybbert, I made a custom page template because I hate Divi with a burning passion and I'm sick of overriding things and the code bloat. -Joseph E.

wp_head();
?>

<section id="hero">
  <div class="container">

    <header class="et_pb_row">
      <nav>
        <a href="#" class="logo"><img src="https://nonprofit.eborall.net/wp-content/themes/diviSpecial-child/images/gummishelter-logo-white.svg" alt="GummiShelter Logo"></a>
        <a href="javascript:void(0);" onclick="toggleMenu();" class="toggle"><svg xmlns="http://www.w3.org/2000/svg" width="35.745" height="30" viewBox="0 0 35.745 30"><path class="burger" d="M34.787,72.468H.957A.957.957,0,0,1,0,71.511V68.957A.957.957,0,0,1,.957,68h33.83a.957.957,0,0,1,.957.957v2.553A.957.957,0,0,1,34.787,72.468Zm0,12.766H.957A.957.957,0,0,1,0,84.277V81.723a.957.957,0,0,1,.957-.957h33.83a.957.957,0,0,1,.957.957v2.553A.957.957,0,0,1,34.787,85.234Zm0,12.766H.957A.957.957,0,0,1,0,97.043V94.489a.957.957,0,0,1,.957-.957h33.83a.957.957,0,0,1,.957.957v2.553A.957.957,0,0,1,34.787,98Z" transform="translate(0 -68)"/></svg></a>
        <ul class="menu">
          <li><a href="#mission">Mission</a></li>
          <li><a href="#involved">Get Involved</a></li>
          <li><a href="#testimonials">Testimonials</a></li>
          <li><a href="#adopt" class="button">Adopt Now</a></li>
        </ul>
      </nav>
    </header>

    <div class="et_pb_row">
      <h2>Ending Gummy Animal Abuse,<br> One <a href="#adopt" class="swap">Bear</a> at a Time.</h2>
      <p>Saving Abused Gummy Animals • Finding Loving Homes • Educating the Public</p>
    </div>
    <div class="et_pb_row et_pb_gutters2">
      <div class="et_pb_column et_pb_column_1_2"><a href="#mission" class="button white">Our Mission</a></div>
      <div class="et_pb_column et_pb_column_1_2"><a href="#adopt" class="button">Adopt Now</a></div>
    </div>
  </div>
</section>

<!-- Custom Menu JS -->
<script>
  function toggleMenu() {
    var menu = document.querySelector('.menu');
    menu.classList.toggle('active');
  }

  // Swap Word on Hero
  var wordSwap = function() {
    // Gummy Types
    var gummy_types = ['Worm', 'Fish', 'Bear', 'Shark', 'Lion', 'Hippo'];
    var gummy_length = gummy_types.length;

    // Generate Random Int
    var randomInt = Math.floor((Math.random() * gummy_length));
    document.querySelector('.swap').textContent = gummy_types[randomInt];
  };

  wordSwap();

  // Run wordSwap every 2 secs
  setInterval(wordSwap, 2000);

</script>

<section id="mission">
  <div class="container">
    <div class="et_pb_row">
      <h3>42 million Gummy Animals died from abuse in 2019.<br/>That number is predicted to triple in 2020.</h3>
      <span>Together, we can stop that from happening.</span>
    </div>
    <div class="et_pb_row">
      <video controls poster="https://nonprofit.eborall.net/wp-content/themes/diviSpecial-child/images/poster.jpg">
        <source src="https://nonprofit.eborall.net/wp-content/themes/diviSpecial-child/armsOfTheAngel.mp4" type="video/mp4">
      </video>
    </div>
  </div>
</section>

<section id="involved" class="et_pb_section">
  <div class="container">
    <div class="et_pb_row">
      <h3>3 Ways You Can Make a Difference</h3>
    </div>
    <div class="et_pb_row et_pb_gutters3 illustrations">
      <div class="et_pb_column et_pb_column_1_3 et_pb_column_1">
        <img src="https://nonprofit.eborall.net/wp-content/themes/diviSpecial-child/images/education-illustration.svg" alt="Educate Others">
        <h4>Help Us<br> Educate Others</h4>
        <p>Don’t let them suffer in silence.<br>Spread the word using <a>our scripts</a></p>
      </div>
      <div class="et_pb_column et_pb_column_1_3 et_pb_column_1">
        <img src="https://nonprofit.eborall.net/wp-content/themes/diviSpecial-child/images/abused-illustration.svg" alt="Abused Gummies">
        <h4>Save abused<br> Gummy animals </h4>
        <p>Report cases of gummy<br> animal abuse or neglect by calling 4-2-0</p>
      </div>
      <div class="et_pb_column et_pb_column_1_3 et_pb_column_1">
        <img src="https://nonprofit.eborall.net/wp-content/themes/diviSpecial-child/images/loving-home-illustration.svg" alt="Loving Home">
        <h4>Provide a <br> loving home</h4>
        <p>If you have the means,<br/>adopt a gummy friend</p>
      </div>
    </div>
    <div class="et_pb_row no-top">
      <a href="#adopt" class="button large">Adopt Now</a>
    </div>
  </div>
</section>

<section id="testimonials" class="container">
  <div class="module et_pb_row et_pb_gutters3">
    <div class="et_pb_column"><img src="https://nonprofit.eborall.net/wp-content/themes/diviSpecial-child/images/Ellipse 1@2x.jpg"></div>
    <div class="quote">
      <span>I don’t know where I would be without my Gummy Bear, Toby. </span>
      <p>Karen S.</p>
    </div>
  </div>
</section>

<section id="adopt">
  <div class="container">
    <div class="et_pb_row">
      <h1>Adopt a Gummy Animal</h1>
      <p>Find your next best friend by giving a home to an abused Gummy Animal</p>
    </div>
 
    <!-- WP Loop -->
    <?php
    $args=array(
      'post_type' => 'gummi',
      'post_status' => 'publish',
      'posts_per_page' => 9,
      'orderby' => 'rand'
      );

    $my_query = null;
    $my_query = new WP_Query($args);

    if( $my_query->have_posts() ) {

      $i = 0;
      while ($my_query->have_posts()) : $my_query->the_post();

    if($i % 3 == 0) { ?> 

    <div class="et_pb_row et_pb_gutters3">

    <?php
    }
    ?>

      <div class="et_pb_column et_pb_column_1_3 et_pb_column_1 card" href="">
        <div class="avatar">
          <img src="<?php echo get_post_meta( get_the_ID(), 'wpcf-profile-pic', true);?>"/>
        </div>  
        <div class="desc">
          <h5 class="title"><?php the_title_attribute(); ?></h5>
          <p><?php the_content(); ?></p>
          <a href="javascript:void(0);" onclick="checkout('<?php the_title_attribute(); ?>')" class="button"><img src="https://nonprofit.eborall.net/wp-content/themes/diviSpecial-child/images/heart.svg" height="18"/>Adopt</a>
        </div>
      </div>  

  <?php $i++; 
  if($i != 0 && $i % 3 == 0) { ?>
    </div>
  <?php
  } ?>

  <?php  
    endwhile;
    }
    wp_reset_query();
    ?>

  </div>
</section>

<!-- Custom Checkout Modal -->
<aside class="checkout">
  <div>
    <h6>Thank you for adopting<br><span class="gummy-name">{{gummy.name}}</span>!!</h6>
    <p>You're making a difference!</p>
    <a href="javascript:void(0);" onclick="removeCheckout()"><img src="https://nonprofit.eborall.net/wp-content/themes/diviSpecial-child/images/times.svg" width="30" alt="Close"></a>
  </div>
</aside>

<!-- Checkout Modal JS -->
<script>
  window.addEventListener('click', function(event) {
    if (document.querySelector('.checkout').classList.contains('active') && !event.target.classList.contains('button'))  {
      removeCheckout();
    }
  });

  function checkout(gummyName) {
    var nameReplacement = document.querySelector('.checkout');
    nameReplacement.classList.toggle('active');

    document.querySelector('.gummy-name').textContent = gummyName;
  }

  function removeCheckout() {
    document.querySelector('.checkout').classList.remove('active');
  }
</script>

<?php
get_footer();
?>
