const gulp = require('gulp');
const imagemin = require('gulp-imagemin');
const imageminGuetzli = require("imagemin-guetzli");
const sass = require('gulp-sass');
const concat = require("gulp-concat");

sass.compiler = require('node-sass');

// Optimize Images
gulp.task("optimize", () =>
  gulp
    .src("images/**/*")
    .pipe(
      imagemin([
        imageminGuetzli({ quality: 84 }),
        imagemin.optipng({ optimizationLevel: 5 }),
        imagemin.svgo({
          plugins: [{ removeViewBox: true }, { cleanupIDs: false }]
        })
      ])
    )
    .pipe(gulp.dest("dist/images"))
);

// Sass Compile
gulp.task('sass', () =>
  gulp.src('./stylesheets/main.scss')
  .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
  .pipe(concat('style.css'))
  .pipe(gulp.dest('.'))
);