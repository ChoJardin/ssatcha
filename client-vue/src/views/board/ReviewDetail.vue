<template>
  <div class="container-fluid">
    <img class="backdrop" :src="full_backdroppath" width="100%">
    <!--리뷰-->
    <div class="reviewdetail">
        <br><br><br>
      <div class="ms-3" style="margin-top: 30px">
        <!--영화제목-->
        <div @click="setMovieDetail(review.movie.id)" class="h3 d-inline-block">
          <RouterLink :to="`/${review.movie.id}`" class="text-decoration-none">
            <h2 class="review-title">{{ review.movie.title }}</h2>
          </RouterLink>
        </div>

        <!--리뷰상세-->
        <div class="about-review">
          <span class="review-semititle fw-bolder">리뷰 제목 : </span>
          <span class="reviewdetail">{{ review.title }}</span>
          <br>
          <span class="review-semititle fw-bolder">평가 : </span>
          <span class="reviewdetail">{{ review.rank }}</span>
          <br>
          <p class="review-semititle fw-bolder mt-1">리뷰 내용</p>
          <span class="reviewdetail">{{ review.content }}</span>
        </div>
      </div>

      <!--좋아요 및 작성일자-->
      <div class="container-fluid d-inline-block d-flex justify-content-between">
        <!--좋아요 버튼-->
        <div>
        <br>
          <!--로그인 했을 때-->
          <div v-if="isLoggedIn" class="d-inline-block">
            <!--좋아요-->
            <span v-if="isReviewLiked" @click="likeReview(commentData)" >
              이 리뷰 별로에요
              <img src="@/assets/LOGO_black.png" width="25vh" class="ms-1 me-3 sm-content likebtn">
            </span>
            <span v-else @click="likeReview(commentData)" >
              이 리뷰 좋아요
              <img src="@/assets/LOGO_red.png" width="25vh" class="ms-1 me-3 sm-content likebtn">
            </span>
            <!--리뷰 수정-->
            <span v-if="review.user === $store.state.accounts.loginUser.id">
              이 리뷰 수정하기
              <img src="@/assets/LOGO_VER1.png" @click="editReview" width="25vh" class="ms-1 me-3 sm-content likebtn">
            </span>
            <span>
              이 리뷰 삭제하기
              <img src="@/assets/LOGO_black.png" @click="deleteReview(review)" width="25vh" class="ms-1 me-3 sm-content likebtn">
            </span>
          </div>

          <!--비로그인-->
          <div v-else class="d-inline-block">
            <h5>
              리뷰에 좋아요를 누르려면 <a href="/accounts/login">로그인</a>이 필요합니다.
            </h5>
          </div>
        </div>
        <!--작성일자-->
        <div>
          <br>
          <!-- <span class="datetime">작성일:{{ review.created_at }}</span> -->
          <span class="datetime">작성일: {{ created_date }}</span>
          <br>
          <!-- <span class="datetime">수정일: {{ review.updated_at }}</span> -->
          <span class="datetime">수정일: {{ updated_date }}</span>
        </div>
      </div>
      <!--좋아요 및 작성일자 종료-->

      <hr>

      <!--댓글-->
      <div class="ms-2 mb-2">
        <h4 class="mb-3">쌓인 댓글 보기</h4>
        <!--댓글 입력-->
        <div class="comment-input my-2">
          <!--로그인-->
          <div v-if="isLoggedIn">
            <div class="input-group">
              <input class="form-control comment-input" v-model="commentData.content" @keyup.enter="[createComment(commentData), onSubmit()]"/>
              <div class="input-group-append">
                <button @click="[createComment(commentData), onSubmit()]" class="btn btn-comment">댓글 달기</button>
              </div>
            </div>
          </div>
          <!--비로그인-->
          <div v-else>
            <h5> 댓글을 달기 위해서는 <a href="/accounts/login">로그인</a>이 필요합니다.</h5>
          </div>
        </div>
        <!--댓글 보여주기-->
        <div v-if="isCommented">
          <div class="mt-2">
            <hr>
            <div v-for="(comment, idx) in notNestedComments" :key="idx">
              <CommentItem :comment="comment"/>
            </div>
          </div>
        </div>
        <!--댓글 보여주기-->
      </div>
      <!--댓글-->
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState } from "vuex";
import CommentItem from "@/components/boards/CommentItem";

export default {
  name: "ReviewDetail",
  components: {
    CommentItem,
  },
  data() {
    return {
      review: {
        movie: {
          id: '',
          title: '',
        },
      },
      commentData: {
        movie: '',
        review: '',
        reply_to: '',
        content: '',
      },
    }
  },
  methods: {
    ...mapActions(['createComment', 'fetchReview', 'likeReview', 'setMovieDetail']),
    onSubmit() {
      this.commentData.content = ''
    },
    editReview() {
      this.$router.push({ name: 'UpsertReview', params: { isUpdate: true, movie_id: this.commentData.movie, review: this.review }})
    },
    deleteReview() {
      if (confirm('정말 삭제하시겠습니까?')) {
        this.$store.dispatch('deleteReview', this.review)
      }
    },
  },
  computed: {
    ...mapState({selectedReview: state => state.boards.selectedReview}),
    ...mapGetters(['isReviewLiked', 'notNestedComments', 'getMovieId', 'isLoggedIn']),
    isCommented() {
      return !!this.review.comment_set;
    },
    full_backdroppath() {
      return "https://image.tmdb.org/t/p/original/" + this.review.movie.backdrop_path
    },
    created_date() {
      return this.review.created_at.substring(0,10)
    },
    updated_date() {
      return this.review.updated_at.substring(0,10)
    },
  },
  watch: {
    '$store.state.boards.selectedReview': function() {
        this.review = this.selectedReview
    }
  },
  created() {
    this.commentData.movie = this.$route.params.movie_id
    this.commentData.review = this.$route.params.review_id
    if (this.selectedReview) {
      this.review = this.selectedReview
    }
  },

}
</script>

<style scoped>
.review-title {
  color: #3396f4;
}

.reviewdetail {
  position: relative;
  font-family: 'Noto Sans KR', sans-serif;
  color: rgb(255, 255, 255);
  z-index: 99;
  font-weight: 100;
}

.backdrop {
  position: absolute;
  opacity: 0.1;
  z-index: 1;
  margin-top: 80px;
}

.about-review {
  position: relative;
  z-index: 100;
  font-size: 20px;
}

.review-semititle {
  font-weight: 300;
  font-size: 20px;
  color: #3396f4;
  /* text-shadow: 1.5px 1.5px 1.5px rgb(113, 114, 114); */
}

.datetime {
  font-size: 15px;
  text-align: right;
}

.comment-input {
  vertical-align: middle;
  background-color: transparent;
}

.comment-input:hover {
  color: white;
  background-color: #3397f411;
  border: 0.5px solid #3396f4;
}

.likebtn {
  position: relative;
  z-index: 100;
  cursor: pointer;
}

.btn-comment {
  color: aliceblue;
  background-color: #3396f4;
  border-radius: 1px;
}
</style>