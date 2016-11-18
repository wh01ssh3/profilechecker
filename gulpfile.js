var gulp = require('gulp');
var cleanCSS = require('gulp-clean-css');

gulp.task('css', function () {
    // Build css
    gulp.src('assets/css/style.css').pipe(cleanCSS()).pipe(gulp.dest('static/css'));
});

gulp.task('default', function () {
    // Default task
    gulp.run('css');
});