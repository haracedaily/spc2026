        let interval;
        let timerId;
        const timeInput = document.getElementById("timeInput");
        const progress = document.getElementById("progress");
        const startBtn = document.getElementById("startBtn");
        const clearBtn = document.getElementById("clearBtn");

        startBtn.addEventListener('click',startProgress);
        clearBtn.addEventListener('click',clearProgress);
        function startProgress(){
            startBtn.disabled=true;
            console.log(timeInput);
            duration = parseInt(timeInput.value);
            console.log("입력초 : ", duration);

            let elapsed = 0;

            timerId = setInterval(()=>{
                elapsed++;
                const ratio = ((elapsed / duration) * 100);
                progress.style.width = `${ratio}%`;
                progressText.textContent = `${Math.floor(ratio,2)}%`;
                console.log(progress);
                if(ratio>=100){
                    clearInterval(timerId);    
                    startBtn.disabled=false;
                }
            },1000)
        }

        function clearProgress(){
            progress.style.width='2px';
            timeInput.value="";
            progressText.textContent="0%";
            clearInterval(timerId);
            startBtn.disabled=false;
        }
        // clearInterval(timerId);