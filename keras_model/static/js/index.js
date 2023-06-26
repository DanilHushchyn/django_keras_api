import {upload} from "./upload.js";

upload('.form__horizontal-img',{
    multiple: false,
    accept: ['.png','.jpg','.jpeg','.svg']
})