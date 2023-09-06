import "./Image.css";
import LoadingSpinner from "../component/Spinner";

import { useState } from "react";
import axios from "axios";


const Image = () => {
    const [imageSrc,setImageSrc] = useState(null);
    const [imgName,setImgName] = useState('')
    const [isLoading, setIsLoading] = useState(false);

    const requestConfig = {
    timeout: 60000, 
    };

    const check = async () =>{
        try{  
            setIsLoading(true)
            const formData = new FormData();
            formData.append('imageFile', imageSrc);
    
            const response = await axios.post("http://127.0.0.1:5002/get-image",formData,requestConfig)
            
            setIsLoading(false)
            setImgName(response.data.prediction)
        }catch(error){
            setIsLoading(false)
            console.log(error);
        }
    }


    const handleImageChange = (e) => {
        const selectedFile = e.target.files[0];
        
        if (selectedFile && selectedFile.type.startsWith('image/')) {
            setImageSrc(selectedFile);
        } else {
        alert('Please select a valid image file.');
            setImageSrc(null);
        }
    };

    return (
        <div className="hello">
            <div className="img">{imageSrc ? <img srcSet={URL.createObjectURL(imageSrc)} sizes="(max-width:600px) 480px,800px" alt="Image" />: <>not found</> }</div>
            <div className="upload-check">
                <div className="upload-btn-wrapper">
                    <button class="btn">Upload a file</button>
                    <input type="file" accept="image/*" onChange={(e) => handleImageChange(e)}></input>
                </div>
                <div>
                    <button className="btn" onClick={()=> check()}>Check the image</button>
                </div>
            </div>
            <div className="prediction">
                {isLoading ? <LoadingSpinner />: 
                    imgName && <h3>Prediction is : {imgName}</h3> }
            </div>
        </div>
    )
}

export default Image;