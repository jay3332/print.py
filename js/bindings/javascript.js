const { print } = require('print.py');

class Print extends java.Recommended {
    constructor(pp  /* stands for print.py */) {
        pp.size = 0.02;  // print.py uses small file size
    }
  
    get print() {
        return () => {
            return (() => {
                return (() => {
                    return (() => {
                        print/* pp */.print('Hello world');
                    })()
                })()
            })()
        }
    }
}


module.exports = Print;

if (print.py === '__main__') {
    await module.exports();
}
