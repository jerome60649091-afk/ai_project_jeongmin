// HTML에서 필요한 요소를 찾아 변수에 저장합니다.
const nameInput = document.getElementById("nameInput");
const startButton = document.getElementById("startButton");
const messageArea = document.getElementById("resultArea");

// 화면에 메시지를 보여주는 함수입니다.
function showMessage(text, type) {
  // 기존 메시지를 지웁니다.
  messageArea.innerHTML = "";

  // 새 메시지 박스를 만듭니다.
  const messageBox = document.createElement("div");
  messageBox.className = "message-box " + type;
  messageBox.textContent = text;

  // 메시지 박스를 화면에 추가합니다.
  messageArea.appendChild(messageBox);
}

// 버튼을 눌렀을 때 실행되는 함수입니다.
function handleStartClick() {
  // 입력값의 앞뒤 공백을 제거합니다.
  const name = nameInput.value.trim();

  if (name) {
    showMessage(name + "님, 환영합니다! AI 협업 개발 실습을 시작합니다.", "message-success");
  } else {
    showMessage("이름을 입력한 뒤 다시 시도해주세요", "message-warning");
  }
}

// 버튼 클릭 이벤트를 연결합니다.
startButton.addEventListener("click", handleStartClick);
