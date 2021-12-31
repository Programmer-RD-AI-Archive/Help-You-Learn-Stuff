import { Button, Col, Container, Row } from "react-bootstrap";
import NavBar from "../components/NavBar/NavBarHYLS";
import "./Home.css";
const Home = () => {
  return (
    <>
      <NavBar />
      <div className="bg-img">
        <div className="bg-text">
          <h1>
            A Platform to Help <br /> <b>You</b> <br /> Learn Any Subject you
            want
          </h1>
          <h4>
            <b> Discover your Passion </b>
          </h4>
          <Container>
            <Row>
              <Col xs>
                <a href="/Sign/Up">
                  <Button variant="outline-secondary">
                    <h3>Sign Up</h3>
                  </Button>
                </a>
              </Col>
              <Col xs={{ order: 1 }}>
                <a href="/Login">
                  <Button variant="outline-dark">
                    <h3>Login</h3>
                  </Button>
                </a>
              </Col>
            </Row>
          </Container>
        </div>
      </div>
    </>
  );
};

export default Home;
