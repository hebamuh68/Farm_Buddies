import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import Row from "react-bootstrap/Row";
import "./Partner_form.css";

function Partner_Form() {
  return (
    <>
      <div className="container">
        <Form>
          <Row className="mb-3">
            <Form.Group as={Col} controlId="formGridEmail">
              <Form.Label>Full Name</Form.Label>
              <Form.Control type="text" placeholder="full name" />
            </Form.Group>

            <Form.Group as={Col} controlId="formGridEmail">
              <Form.Label>Email</Form.Label>
              <Form.Control type="email" placeholder="Enter email" />
            </Form.Group>
          </Row>

          <Row className="mt-4">
            <Form.Group as={Col} controlId="formGridState">
              <Form.Label>Governorate</Form.Label>
              <Form.Select defaultValue="Choose...">
                <option>Choose...</option>
                <option>Assiut</option>
                <option>Alexandria</option>
                <option>Aswan</option>
                <option>Beheira</option>
                <option>Bani Suef</option>
                <option>Cairo</option>
                <option>Daqahliya</option>
                <option>Damietta</option>
                <option>Fayyoum</option>
                <option>Gharbiya</option>
                <option>Giza</option>
                <option>Helwan</option>
                <option>Ismailia</option>
                <option>Kafr El Sheikh</option>
                <option>Ismailia</option>
                <option>Luxor</option>
                <option>Marsa Matrouh</option>
                <option>Minya</option>
                <option>Monofiya</option>
                <option>New Valley</option>
                <option>North Sinai</option>
                <option>Port Said</option>
                <option>Qalioubiya</option>
                <option>Qena</option>
                <option>Red Sea</option>
                <option>Sharqiya</option>
                <option>Sohag</option>
                <option>South Sinai</option>
                <option>Suez</option>
                <option>Tanta</option>
              </Form.Select>
            </Form.Group>

            <Form.Group as={Col} controlId="formGridState">
              <Form.Label>Gender</Form.Label>
              <Form.Select defaultValue="Choose...">
                <option>Choose...</option>
                <optionl>Female</optionl>
                <option>Male</option>
              </Form.Select>
            </Form.Group>
          </Row>

          <Row className="mt-4">
            <Form.Group as={Col} controlId="formGridState">
              <Form.Label>CS Field</Form.Label>
              <Form.Select defaultValue="Choose...">
                <option>Choose...</option>
                <option>Front-end</option>
                <option>Front-end - React</option>
                <option>Front-end - Angular</option>
                <option>Front-end - Vue</option>

                <option></option>

                <option>Back-end</option>
                <option>Back-end - Node.js</option>
                <option>Back-end - Ruby </option>
                <option>Back-end - Django</option>
                <option>Back-end - Laravel</option>
                <option>Back-end - Flask</option>
                <option>Back-end - Express.js</option>
                <option>Back-end - Spring</option>
                <option>Back-end - PHP</option>

                <option></option>

                <option>Full-stack</option>
                <option>Full-stack - MERN Stack</option>
                <option>Full-stack - LAMP Stack</option>

                <option></option>

                <option>Mobile dev</option>
                <option>Mobile dev- IOS</option>
                <option>Mobile dev- Flutter</option>
                <option>Mobile dev- React Native</option>
                <option>Mobile dev- Kotlin/Java</option>

                <option></option>

                <option>DevOps</option>
                <option>Quality assurance (QA)</option>
                <option>Data science</option>
                <option>Machine learning</option>
                <option>Cybersecurity</option>
              </Form.Select>
            </Form.Group>

            <Form.Group as={Col} controlId="formGridState">
              <Form.Label>Experience level</Form.Label>
              <Form.Select defaultValue="Choose...">
                <option>Choose...</option>
                <optionl>Undergraduate</optionl>
                <option>Senior student</option>
                <option>Entry-level</option>
                <option>Mid-level</option> <option>Entry-level</option>{" "}
                <option>Senior-level</option>
                <option>Managerial-level</option>
                <option>Executive-level</option>
              </Form.Select>
            </Form.Group>
          </Row>

          <Row className="mt-4 mb-4">
            <Form.Group as={Col} controlId="formGridEmail">
              <Form.Label>Github</Form.Label>
              <Form.Control type="text" placeholder="add link" />
            </Form.Group>

            <Form.Group as={Col} controlId="formGridEmail">
              <Form.Label>Linkedin </Form.Label>
              <Form.Control type="text" placeholder="add link" />
            </Form.Group>

            <Form.Group as={Col} controlId="formGridEmail">
              <Form.Label>Twitter</Form.Label>
              <Form.Control type="text" placeholder="add link" />
            </Form.Group>
          </Row>

          {/*           <Form.Group className="mb-3" id="formGridCheckbox">
            <Form.Check type="checkbox" label="Check me out" />
          </Form.Group> */}

          <Button className="btn btn-primary" type="submit">
            Submit
          </Button>
        </Form>
        <img id="play" alt="" src={require("../images/Hero/play.gif")} />
      </div>
    </>
  );
}

export default Partner_Form;
