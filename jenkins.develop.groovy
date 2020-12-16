def build_app(){
  sh 'docker-compose up -d'
}

def test_app(){
  sh 'python test_app.py'
}

def down_app(){
  sh 'docker-compose down'
}

def release_app(){
  echo 'branch into release'
}

def live_app(){
}

return this