// HTML에서 필요한 요소들을 찾아서 변수에 저장합니다
const nameInput   = document.getElementById("nameInput");   // 이름 입력 필드
const startButton = document.getElementById("startButton"); // 실습 시작 버튼
const messageArea = document.getElementById("resultArea");  // 메시지를 표시할 영역

// 요소를 하나라도 찾지 못하면 오류 메시지를 남기고 실행을 멈춥니다
if (!nameInput || !startButton || !messageArea) {
  console.error("필요한 HTML 요소를 찾지 못했습니다. id 값을 확인해주세요.");
} else {
  // 버튼을 클릭하면 handleStartClick 함수를 실행합니다
  startButton.addEventListener("click", handleStartClick);
}

// 화면에 메시지 박스를 보여주는 함수입니다
// text: 표시할 문장, type: 스타일 종류("message-success" 또는 "message-warning")
function showMessage(text, type) {
  // 이전에 표시된 메시지를 지웁니다
  messageArea.innerHTML = "";

  // 새 메시지 박스 요소를 만듭니다
  const messageBox = document.createElement("div");

  // 기본 스타일 클래스와 종류별 스타일 클래스를 함께 적용합니다
  messageBox.className = "message-box " + type;

  // 메시지 내용을 설정합니다
  messageBox.textContent = text;

  // 메시지 박스를 화면에 추가합니다
  messageArea.appendChild(messageBox);
}

// 버튼을 클릭했을 때 실행되는 함수입니다
function handleStartClick() {
  // 입력 필드의 값을 가져오고, 앞뒤 공백을 제거합니다
  const name = nameInput.value.trim();

  if (name) {
    // 이름이 입력된 경우: 성공 메시지를 초록색으로 표시합니다
    showMessage(name + "님, 환영합니다! AI 협업 개발 실습을 시작합니다.", "message-success");
  } else {
    // 이름이 비어 있는 경우: 경고 메시지를 노란색으로 표시합니다
    showMessage("이름을 먼저 입력해주세요.", "message-warning");
  }
}