def build_app(){
  bat 'docker-compose up -d'
}

def test_app(){
  bat 'python test_app.py'
}

def down_app(){
  bat 'docker-compose down'
}

def release_app(){
  echo 'branch into release'
}

def live_app(){
}

return this