const go = new Go();

class Random {
    constructor(seed = 1487256) {
        this.x = 123456789;
        this.y = 362436069;
        this.z = 521288629;
        this.w = seed;
    }

    next() {
        let t;
    
        t = this.x ^ (this.x << 11);
        this.x = this.y; this.y = this.z; this.z = this.w;
        return this.w = (this.w ^ (this.w >>> 19)) ^ (t ^ (t >>> 8)); 
    }

    nextInt(min, max) {
        const r = Math.abs(this.next());
        return min + (r % (max + 1 - min));
    }
}

WebAssembly.instantiateStreaming(fetch("wasm/main.wasm"), go.importObject).then((result) => {
    go.run(result.instance);
    
    // Hmm, I wish I could get a list of wasm functions...

    const element = document.getElementById("dummy");
    let text = window.getComputedStyle(element, ':before').getPropertyValue('content');
    if(!(text == "\"FLAG{tHis_15_DuMmy}\"" || text == "\"FLAG{7h15_Is_dUMmY}\"")){
        element.style.display = "none";

        let array = text.split("");
        let array2 = [];
        const random = new Random(getNumber());
        for(let i = 1; i < array.length - 1; i++){
            array2[i] = String.fromCharCode(array[i].charCodeAt() - random.nextInt(2, 10));
        }
        let flag = array2.join("");
        document.getElementById("flag").innerText = flag;
    }
});
