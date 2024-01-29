modal_btn_cancel.addEventListener("click", function() {
	modal.style.display = "none";
})

class Timer {
constructor(root) {
    root.innerHTML = Timer.getHTML();

    this.el = {
    minutes: root.querySelector(".timer__part--minutes"),
    seconds: root.querySelector(".timer__part--seconds"),
    control: root.querySelector(".timer__btn--control"),
    reset: root.querySelector(".timer__btn--reset"),
    modal: root.querySelector("#modal_chronometer"),
    modal_btn_cancel: root.querySelector("#cancel_modal"),
    minute: 0,
    second: 0,
    first_m: 0,
    first_s: 0,
    };

    this.interval = null;
    this.remainingSeconds = 0;

    this.el.control.addEventListener("click", () => {
    if (this.interval === null) {
        this.start();
    } else {
        this.stop();
    }
    });

    this.el.reset.addEventListener("click", () => {
    const inputMinutes = prompt("Enter number of minutes:");

    if (inputMinutes < 60) {
        var c = true;
        this.stop(c);
        this.remainingSeconds = inputMinutes * 60;

        this.el.first_m = Math.floor(this.remainingSeconds / 60).toString().padStart(2, "0");
        this.el.first_s = (this.remainingSeconds % 60).toString().padStart(2, "0");
        
        this.updateInterfaceTime();
    }
    });
}

updateInterfaceTime() {
    var minutes = Math.floor(this.remainingSeconds / 60);
    var seconds = this.remainingSeconds % 60;
    this.el.minute = minutes.toString().padStart(2, "0");
    this.el.second = seconds.toString().padStart(2, "0");

    this.el.minutes.textContent = this.el.minute;
    this.el.seconds.textContent = this.el.second;
}

updateInterfaceControls(c) {
    if (this.interval === null) {
    this.el.control.innerHTML = `<span class="material-icons">play_arrow</span>`;
    this.el.control.classList.add("timer__btn--start");
    this.el.control.classList.remove("timer__btn--stop");
    if (c != true) {
        modal.style.display = "initial";

        var minute_area = document.querySelector("#minute")
        var second_area = document.querySelector("#second")
        
        minute_area.value = this.el.first_m
        second_area.value = this.el.first_s
    }
    
    
    } else {
    this.el.control.innerHTML = `<span class="material-icons">pause</span>`;
    this.el.control.classList.add("timer__btn--stop");
    this.el.control.classList.remove("timer__btn--start");
    
    }
}

start() {
    if (this.remainingSeconds === 0) return;

    this.interval = setInterval(() => {
    this.remainingSeconds--;
    this.updateInterfaceTime();

    if (this.remainingSeconds === 0) {
        this.stop();
    }
    }, 1000);

    this.updateInterfaceControls();
}

stop(c) {
    clearInterval(this.interval);

    this.interval = null;

    this.updateInterfaceControls(c);
}

static getHTML() {
    return `
            <span class="timer__part timer__part--minutes">00</span>
            <span class="timer__part">:</span>
            <span class="timer__part timer__part--seconds">00</span>
            <button type="button" class="timer__btn timer__btn--control timer__btn--start">
                <span class="material-icons">play_arrow</span>
            </button>
            <button type="button" class="timer__btn timer__btn--reset">
                <span class="material-icons">timer</span>
            </button>
        `;
}
}

new Timer(
    document.querySelector(".timer")
);






