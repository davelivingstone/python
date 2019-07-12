/* I ported my pyramid.py script to JavaScript.
All it needs is some html to insert it into.
Of course, we could use #s or 8s or Ds instead of *s as
building blocks.
I know, it's horrible with all those parentheses.
Still thinking about a possible refactoring.*/

function pyramid(n){
    for(let i = 1; i <= n; i+=2){
        console.log(' '.repeat(Math.floor(((n-i)/2))) + '*'.repeat(i) + ' '.repeat(Math.floor(((n-i)/2))));
    }
};

