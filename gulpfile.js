var gulp = require('gulp');

gulp.task('css', function () {
    // Build css
    gulp.src('assets/src/css/style.css').pipe(gulp.dest('assets/build/css'));
});

gulp.task('default', function () {
    // Default task
    gulp.run('css');
});